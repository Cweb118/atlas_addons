import os
import asyncio
from datetime import datetime

async def run_cmd(cmd):
    try:
        log_name = cmd.replace('.py', '_log.txt')
        logtxt = cmd+" start time: "+str(datetime.now())+'\n'
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
        logtxt += cmd+" end time: "+str(datetime.now())
        logfile.write(logtxt)
        logfile.close()
    except asyncio.CancelledError:
        proc.terminate()
        print("Process Terminated")

async def main():
    subfolder_run_files = SUBPROCESS_LIST
    await asyncio.gather(*[run_cmd(x) for x in subfolder_run_files])

asyncio.run(main())
