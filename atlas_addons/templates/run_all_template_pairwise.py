import os
import asyncio
from datetime import datetime

#===============
#
# File: run_all_template_pairwise.py
# Version: 1.0, 08-22-22
# Usage (cmd): python <filename>
# Description: On run this script trigger each run_template whose path has been written to this file upon running a project_init script
#              Pairwise: Pairs (or sets) of installed run_template files will be run in parallel, with subsequent sets running in sequence
#
# Authors: Caleb Weber, Oleksandr Savytskyi, Ph.D, Thomas Caulfield, Ph.D
# CAULFIELD LABORATORY, PROPERTY OF MAYO CLINIC
# https://www.mayo.edu/research/labs/drug-discovery-design-optimization-novel-therapeutics-therapeutics
#
#===============

async def run_cmd(cmd):
    try:
        log_name = cmd.replace('.py', '_log.txt')
        starttime = datetime.now()
        logtxt = "Start Time: "+str(starttime)+'\n'
        logfile = open(log_name, "w")

        proc = await asyncio.create_subprocess_shell(
            "python "+cmd,
            shell=True,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE)
        stdout, stderr = await proc.communicate()
        msg = f'[{cmd!r} exited with {proc.returncode}]'
        print(msg)
        logtxt += msg+'\n'
        if stdout:
            msg = f'[stdout]\n{stdout.decode()}'
            print(msg)
            logtxt += msg+'\n'
        if stderr:
            msg = f'[stderr]\n{stderr.decode()}'
            print(msg)
            logtxt += msg+'\n'
        endtime = datetime.now()
        logtxt += "End Time: "+str(endtime)+'\n'

        endtime = datetime.now()
        duration = endtime - starttime
        duration_in_s = duration.total_seconds()
        days = divmod(duration_in_s, 86400)
        hours = divmod(days[1], 3600)
        minutes = divmod(hours[1], 60)
        seconds = divmod(minutes[1], 1)
        print("Run Duration: %d days, %d hours, %d minutes and %d seconds" % (days[0], hours[0], minutes[0], seconds[0]))
        logtxt += "Run Duration: "+str(days[0])+" days, "+str(hours[0])+" hours, "+str(minutes[0])+" minutes, "+str(seconds[0])+" seconds"

        logfile.write(logtxt)
        logfile.close()
    except asyncio.CancelledError:
        proc.terminate()
        print("Process Terminated")

async def main():
    subfolder_run_files = SUBPROCESS_LIST
    for pair in subfolder_run_files:
        print("Starting Atlas Analysis for: "+str(pair))
        await asyncio.gather(*[run_cmd(x) for x in pair])
        print("Atlas Analysis Concluded for: "+str(pair))

asyncio.run(main())
