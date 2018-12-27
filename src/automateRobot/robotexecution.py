#!/usr/bin/env python

import os
import sys
import glob

OUTPUT_DIR = os.path.join(os.path.abspath('.'), 'output')

def robot_execute(cases):
    local_repo = r"D:\robot_case"
    rc_code = 0
    if cases is None:
        rc_code = os.system("robot {}".format(local_repo))
    else:
        cases = cases[1:-1]
        cases = cases.replace('\'','')
        cases = cases.split(',')
        for case in cases:
            case = case.strip()
            tmp_rc_code = os.system("robot -d {} -o {}_output.xml -t {} {}".format(OUTPUT_DIR, case, case, local_repo))
            if tmp_rc_code != 0:
                rc_code = tmp_rc_code

    return rc_code

def report_combine():
    xml_files = ""
    for filename in glob.glob(r'{}/*.xml'.format(OUTPUT_DIR)):
        xml_files = xml_files + " " + filename
    os.system("rebot --merge --output output.xml {}".format(xml_files))

if __name__ == '__main__':
    cases = None
    if len(sys.argv) != 1:
        args = sys.argv[1].strip()
        if bool(args):
            cases = sys.argv[1]
    rc_code = robot_execute(cases)
    report_combine()
    exit(rc_code)