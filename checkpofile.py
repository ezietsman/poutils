#!/usr/bin/env python
import sys

import polib
import re

def getTagsInStr(strng):
    '''find all the special tags given a string'''
    tags = re.compile('<_:(.*?)/>').findall(strng)
    tags.sort()
    return tags

    

def specialTagsMatch(entry):
    '''Returns True of the number of special tags in the msgid and msgstr
    are the same. Tags looks like <_:something-1/>
    '''
    msgstr = entry.msgstr
    msgid = entry.msgid
    
    msgTags = getTagsInStr(msgstr)
    idTags = getTagsInStr(msgid)
    if msgTags != idTags:
        print "Entry does not contain similar tags in str and id:\n %s" %entry
        return False

    # count tag occurences based upon opening and closing tags
    openTagsInStr = msgstr.count(r'<_:')
    closeTagsInStr = msgstr.count(r'/>')

    openTagsInId = msgid.count(r'<_:')
    closeTagsInId = msgid.count(r'/>')
    
    if openTagsInStr != closeTagsInStr:
        print "Opening and closing tag mismatch in entry.msgstr:\n%s"%entry
        return False

    if openTagsInId != closeTagsInId:
        print "Opening and closing tag mismatch in entry.msgid:\n%s"%entry
        return False

    if openTagsInStr != openTagsInId:
        print "Tag count mismatch in msg and id in entry: %s" % entry
        return False
    else:
        return True

if __name__ == "__main__":
    prog, filename = sys.argv
    
    if len(sys.argv) != 2:
        print "Usage: %s yourfile.po\n\ntries to find erroneous entries"%sys.argv[0]

    pofile = polib.pofile(filename)

    for entry in pofile:
        checked = specialTagsMatch(entry)

