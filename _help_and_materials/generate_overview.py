import os
import fnmatch
import io
import re

# constants
rootOfGithub = 'https://github.com/admin-shell-io/submodel-templates/tree/main/'

topReadmeFn = '../README.md'
topReadmeHeader = 'Table of IDTA Submodel templates'

class Badge:
     def __init__(self):
          self.Name = ""
          self.Link = ""

class TableEntry:
     def __init__(self):
          self.SmtType = ""
          self.SmtName = ""
          self.Ver = ""
          self.Rev = ""
          self.Badges = []
          self.Link = ""

def process_smt_file(fn, smtType):

     print (f'Reading markdown file {fn} ..')
     file1 = open(fn, 'r')
     lines = file1.readlines()
     
     # make idiotic state machine
     state = 0
     h1 = ''
     h1text = []
     badges = []

     for line in lines:
          ln = line.strip()
          
          if state == 0:
               if ln.startswith('# '):
                    h1 = ln[2:].strip()
                    print(f'  found h1 = {h1}')
                    state = 1
                    continue

          if state == 1:

               # break because found further header
               if ln.startswith('#'):
                    state = 2
                    break

               #find badge?
               m2 = re.match(r'!\[(\w+)\]\(([^)]+)\)', ln)
               if m2:
                    b = Badge()
                    b.Name = m2.group(1)
                    b.Link = m2.group(2)
                    badges.append(b)
                    continue

               # non empty text line
               if len(ln) > 0:
                    h1text.append(ln)

     # ok, SMT folders should reach state 2
     if state != 2:
          return False

     # ok, fn (path) shall allow to determine semantic versioning
     # make sure, all backslashes are slashes
     fn2 = fn.replace('\\', '/')
     match = re.match(r'^((.*)\/([^/]+)\/(\d+)\/(\d+))\/([^/]+)$', fn2)
     if not match:
          return False
     
     smtpath = match.group(1) 
     smtdir = match.group(3)
     ver = match.group(4)
     rev = match.group(5)
     mdfn = match.group(6)

     # for the link, take the full name, but without last part and manually link it to he front
     
     if smtpath.startswith('../'):
          smtpath = smtpath[3:]
     link = rootOfGithub + smtpath

     # ok     

     print (f'Found matching markdown {mdfn} for SMT folder {smtdir} with version / {ver} / {rev} !')

     te = TableEntry()
     te.SmtType = smtType
     te.SmtName = h1
     te.Ver = ver
     te.Rev = rev
     te.Badges = badges
     te.Link = link

     return te

def find_smt(path, smtType):

     print(f'Searching markdown files in {path}')

     res = []

     configfiles = [os.path.join(dirpath, f)
          for dirpath, dirnames, files in os.walk(path)
          for f in fnmatch.filter(files, '*.md')]

     for fn in configfiles:
          te = process_smt_file(fn, smtType)
          if isinstance(te, TableEntry):
               res.append(te)

     return res

class HtmlBuilder:
     def __init__(self):
          self.doc = ""

     def AddHead(self):
          self.doc += """<!doctype html>
<html lang=en>
<head>
<style>
h1 {
     color: #0028cd;
     font-family: Arial, Helvetica, sans-serif;
}

body {
     background-color: #e3e2e2;
     font-size: small;
     font-family: Arial, Helvetica, sans-serif;
}

table {
     font-family: arial, sans-serif;
     border-collapse: collapse;
     width: 100%;
}

th {
     color: #ceced0;
     background-color: #0028cd;
     border: 1px solid #dddddd;
     text-align: left;
     padding: 8px;
}

td {
     border: 1px solid #0028cd;
     color: #0028cd;
     text-align: left;
     padding: 8px;
}

tr:nth-child(even) {
     background-color: #fffff0;
}
tr:nth-child(odd) {
     background-color: #f3f3f3;
}
</style>
<meta charset=utf-8>
<title>blah</title>
</head>
<body>""" + '\n'

     def AddFooter(self):
          self.doc += '</body></html>' + '\n'

     def AddSvgHead(self):
          self.doc += """<svg width="100" height="100" xmlns="http://www.w3.org/2000/svg">
<foreignObject width="100" height="100">
    <div xmlns="http://www.w3.org/1999/xhtml">""" + '\n'

     def AddSvgFooter(self):
          self.doc += """</div>
</foreignObject>
</svg>""" + '\n'

     def AddHeader(self, level, text):
          self.doc += f'<{level}>{text}</{level}>' + '\n'

     def AddTableHeader(self, columns):
          self.doc += '<table style="width:100%"><tr>' + '\n'
          for c in columns:
               self.doc += f'<th>{c}</th>' + '\n'
          self.doc += '</tr>' + '\n'

     def AddTableCells(self, columns):
          self.doc += '<tr>' + '\n'
          for c in columns:
               self.doc += f'<td>{c}</td>' + '\n'
          self.doc += '</tr>' + '\n'

     def AddTableFooter(self):
          self.doc += '</table>' + '\n'

     def AddMdLine(self, line):
          self.doc += '' + line + '\n'

     def AddMdTableHeader(self, columns):
          line = "| "
          for c in columns:
               line += c + " | "
          self.doc += line + '\n'
          line = "| "
          for c in columns:
               line += " ---------- | "
          self.doc += line + '\n'

     def AddMdTableCells(self, columns):
          line = "| "
          for c in columns:
               line += c + " | "
          self.doc += line + '\n'

     def WriteToFile(self, fn):
          f = open(fn, 'w')
          f.write(self.doc)
          f.close()

if __name__ == "__main__":
     print('Starting generator for Submodel template overview')
     print('(c) 2021 by Michael Hoffmeister, Festo SE & Co. KG')

     # whitelist approach
     entries = []
     entries.extend(find_smt('../published', 'Published'))
     entries.extend(find_smt('../development', 'In development'))
     entries.extend(find_smt('../yellow_pages', 'Yellow pages'))

     # make HTML
     html = HtmlBuilder()
     html.AddHead()
     html.AddHeader('h1', topReadmeHeader)
     html.AddTableHeader(['Type SMT', 'Name', 'Version', 'Revision', 'Criteria'])

     for te in entries:

          # prepare Badges
          badges = '' 
          for b in te.Badges:
               badges += f'<img src="{b.Link}">&nbsp;'

          # prepare link for name
          href = f'<a href="{te.Link}">{te.SmtName}</a>'

          html.AddTableCells([te.SmtType, href, te.Ver, te.Rev, badges])

     html.AddTableFooter()
     html.AddFooter()
     html.WriteToFile('overview_Submodel_templates.html')

     # make HTML include
     inc = HtmlBuilder()
     inc.AddMdLine('# ' + topReadmeHeader)
     inc.AddMdLine('')
     inc.AddMdLine('(this table is auto-generated)')
     inc.AddMdLine('')
     inc.AddMdTableHeader(['Type SMT', 'Name', 'Ver', 'Rev', 'Criteria'])

     for te in entries:

          # prepare Badges
          badges = '' 
          for b in te.Badges:
               badges += f'![{b.Name}]({b.Link})  '

          # prepare link for name
          href = f'[{te.SmtName}]({te.Link})'

          inc.AddMdTableCells([te.SmtType, href, te.Ver, te.Rev, badges])

     inc.WriteToFile('overview_Submodel_templates.md')

     # online modify
     if topReadmeFn is not None:

          # read the whole markdown
          with open(topReadmeFn,"r") as f:
               genMd = f.read()

          # can find the correct header; if so, remove the section, add the generated MD
          p = genMd.find('# ' + topReadmeHeader)
          if p > 0:
               # modify
               genMd = genMd[:p]
               genMd += inc.doc

               # only write then
               with open(topReadmeFn,"w") as f:
                    f.write(genMd)

     pass
