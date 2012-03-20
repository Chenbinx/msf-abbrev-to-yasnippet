# -*- coding: utf-8 -*-
# Filename: abbrev_to_ya.py

import re
import os

info = '''
# -*- mode: snippet -*-
# name: memcpy
# contributor: chenbin
# key: memcpy
# group: m
# --'''

abbrev_dir = '.'

str_in_test = '''accept(<field "int SOCKET">, <field "struct sockaddr *ADDR">, <field "socklen_t *LENGTH_PTR">)<endpoint>'''

field_p = r'(<field "([^>"]+)">)'
field_s = r'${\2}'              # replace pattern

endpoint_p = '<endpoint>'
endpoint_s = ';$0'              # replace pattern

def replace_abbrev_to_yasnippet(fn, contributor, abbrev_in):
    """replace abbrev to yasnippet

    Arguments:
    - `fn`: filename
    - `contributor`: user who contribute this file
    - `abbrev_in`: msf-abbrev string
    """
    # first step: replace <field ...>
    ya = re.sub(field_p, field_s, abbrev_in);
    # second step: replace <endpoint>
    ya = re.sub(endpoint_p, endpoint_s, ya);
    # third step: strip newline
    ya = ya.strip('\n')

    name = "# name: %s" % fn
    contributor = "contributor: %s" % contributor
    key = "# key: %s" % fn

    if '_' == fn[0]:
        group = "# group: %s" % ("Others")
    else:
        group = "# group: %s" % fn[0].upper()

    result = ["# -*- mode: snippet -*-",
              name,
              contributor,
              key,
              group,
              "# --",
              ya]
    return '\n'.join(result)


def read_and_write_file(fin):
    """

    Arguments:
    - `fin`:
    """
    with open(fin, 'r') as fi:
        abbrev = fi.read()

        # get rid of x append to filename
        fout = fin
        if 'x' == fin[- 1]:
            fout = fin[:-1]

        ya = replace_abbrev_to_yasnippet(fout,
                                         'heychenbin@gmail.com',
                                         abbrev)
        with open(fout, 'w') as fo:
            fo.write(ya)


if __name__ == '__main__':
    str =  replace_abbrev_to_yasnippet('accept',
                                       'heychenbin@gmail.com',
                                       str_in_test)
    files = os.listdir(abbrev_dir)
    i = 1
    for f in files:
        read_and_write_file(f)
        print '[%d/%d]' % (i, len(files))
        i = i + 1

    
