# from: https://stackoverflow.com/questions/62350872/powershell-file-watcher-register-objectevent-wait-for-file-to-complete-copying

# IMPORTANT: Copy this file to the folder being watchd (typically one level above) and run

Clear-Host
$ErrorActionPreference = [System.Management.Automation.ActionPreference]::Stop

$fileSystemWatcherDirPath = '.'
$fileSystemWatcherFilter = '*.zip'

$fileSystemWatcher = [System.IO.FileSystemWatcher]::new($fileSystemWatcherDirPath , $fileSystemWatcherFilter)
$fileSystemWatcher.IncludeSubdirectories = $true
$fileSystemWatcher.EnableRaisingEvents = $true
$fileSystemWatcher.NotifyFilter = [System.IO.NotifyFilters]::FileName -bor [System.IO.NotifyFilters]::DirectoryName -bor [System.IO.NotifyFilters]::LastWrite  # [System.Linq.Enumerable]::Sum([System.IO.NotifyFilters].GetEnumValues())

# Create syncronized hashtable
# $syncdFsItemEventHashT = [hashtable]::Synchronized([hashtable]::new())
$global:syncdFsItemEventHashT = @{}

$fileSystemWatcherAction = {
    try {
        $fsItemEvent = [pscustomobject]@{
            EventIdentifier  = $Event.EventIdentifier
            SourceIdentifier = $Event.SourceIdentifier
            TimeStamp        = (Get-Date) # $Event.TimeGenerated
            FullPath         = $Event.SourceEventArgs.FullPath
            ChangeType       = $Event.SourceEventArgs.ChangeType
        }

        # Collecting event in synchronized hashtable (overrides existing keys so that only the latest event details are available)
        # $syncdFsItemEventHashT = @{}
        Write-Host $fsItemEvent.FullPath
        Write-Host $syncdFsItemEventHashT
        $syncdFsItemEventHashT[$fsItemEvent.FullPath] = $fsItemEvent
    } catch {
        Write-Host ($_ | Format-List * | Out-String ) -ForegroundColor red
    }
}

# Script block which processes collected events and do further actions like copying for backup, etc...
# That scriptblock was initially used to test "Start-Job". Unfortunately it's not possible to access and modify the synchronized hashtable created within this scope.
$fSItemEventProcessingJob = {
    $keys = [string[]]$syncdFsItemEventHashT.psbase.Keys

    foreach ($key in $keys) {
        $fsEvent = $syncdFsItemEventHashT[$key]

        try {

            Write-Host "Event has TS = ", $fsEvent.TimeStamp

            if ( ( (Get-Date) - $fsEvent.TimeStamp ).TotalSeconds -gt 3) {

                Write-Host "Finally processing: ", $fsEvent.FullPath
                $syncdFsItemEventHashT.Remove($key)

                # do the work
                Remove-Item 'new' -Recurse -ErrorAction SilentlyContinue
                Expand-Archive -Path $fsEvent.FullPath -DestinationPath new
                Set-Location .\new\
                Start-Process -FilePath 'compile-html.bat' -Wait
                Start-Process -FilePath @(Get-ChildItem *.html)[0]
                Set-Location ..
            }

        } catch {
            Write-Host ($_ | Format-List * | Out-String ) -ForegroundColor red
        }
    }
}

[void] (Register-ObjectEvent -InputObject $fileSystemWatcher -EventName 'Created' -SourceIdentifier 'FSCreated' -Action $fileSystemWatcherAction)
[void] (Register-ObjectEvent -InputObject $fileSystemWatcher -EventName 'Changed' -SourceIdentifier 'FSChanged' -Action $fileSystemWatcherAction)
[void] (Register-ObjectEvent -InputObject $fileSystemWatcher -EventName 'Renamed' -SourceIdentifier 'FSRenamed' -Action $fileSystemWatcherAction)
[void] (Register-ObjectEvent -InputObject $fileSystemWatcher -EventName 'Deleted' -SourceIdentifier 'FSDeleted' -Action $fileSystemWatcherAction)

Write-Host "Watching for changes in '$fileSystemWatcherDirPath'.`r`nPress CTRL+C to exit!"
try {
    do {
        Wait-Event -Timeout 1

        if ($syncdFsItemEventHashT.Count -gt 0) {
            Write-Host "`r`n"
            Write-Host ('-' * 50) -ForegroundColor Green
            Write-Host "Collected events in hashtable queue:" -ForegroundColor Green
            $syncdFsItemEventHashT.Values | Format-Table | Out-String
        }

        # Process hashtable items and do something with them (like copying, ..)
        .$fSItemEventProcessingJob

        # Garbage collector
        [GC]::Collect()

    } while ($true)

} finally {
    # unregister
    Unregister-Event -SourceIdentifier 'FSChanged'
    Unregister-Event -SourceIdentifier 'FSCreated'
    Unregister-Event -SourceIdentifier 'FSDeleted'
    Unregister-Event -SourceIdentifier 'FSRenamed'

    # dispose
    $FileSystemWatcher.Dispose()
    Write-Host "`r`nEvent Handler removed."
}
