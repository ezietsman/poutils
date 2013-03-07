#!/usr/bin/env python
import sys

import polib


def chunkIt(seq, num):
    '''Given seq, return num lists of roughly equal size. From http://stackoverflow.com/a/2130035'''
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out



if __name__ == "__main__":
    filename, fullstop, ext = sys.argv[1].partition('.')
    po = polib.pofile(filename+'.'+ext)
    meta = po.metadata

    chunks = chunkIt(po, 5)
    
    for i, chunk in enumerate(chunks):
        outpo = polib.POFile()
        outpo.metadata = meta
        for entry in chunk:
            outpo.append(entry)
        outpo.save('%s-%s.po'%(filename,i))

