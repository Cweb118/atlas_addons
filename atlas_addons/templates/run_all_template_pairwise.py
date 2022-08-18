import os
import asyncio
from datetime import datetime

async def run_cmd(cmd):
    try:
        log_name = cmd.replace('.py', '_log.txt')
        logtxt = "start time: "+str(datetime.now())+'\n'
        starttime_list = [int(datetime.strftime(datetime.now(),'%H')),int(datetime.strftime(datetime.now(),'%M')),int(datetime.strftime(datetime.now(),'%S'))]
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
        logtxt += "end time: "+str(datetime.now())+'\n'
        endtime_list = [int(datetime.strftime(datetime.now(),'%H')),int(datetime.strftime(datetime.now(),'%M')),int(datetime.strftime(datetime.now(),'%S'))]
        logtxt += "run time: "+str((endtime_list[0])-starttime_list[0])+' hours, '+str((endtime_list[1])-starttime_list[1])+' minutes, '+str((endtime_list[2])-starttime_list[2])+' seconds'
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
