#!/usr/bin/env python
import sys

import polib


if __name__ == "__main__":
    file1, file2 = sys.argv[1:3]

    oldpo = polib.pofile(file1)
    newpo = polib.pofile(file2)


    for oldentry in oldpo:
        for newentry in newpo:
            if (oldentry.msgid == newentry.msgid) and (oldentry.msgstr != u""):
                try:
                    newentry.msgstr = oldentry.msgstr
                except:
                    print oldentry.msgstr



    newpo.save('test.po')

