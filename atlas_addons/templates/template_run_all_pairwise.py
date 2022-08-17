import os
import asyncio

async def run_cmd(cmd):
    try:
        proc = await asyncio.create_subprocess_shell(
            "python "+cmd,
            shell=True,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE)
        stdout, stderr = await proc.communicate()
        print(f'[{cmd!r} exited with {proc.returncode}]')
        if stdout:
            print(f'[stdout]\n{stdout.decode()}')
        if stderr:
            print(f'[stderr]\n{stderr.decode()}')
    except asyncio.CancelledError:
        proc.terminate()
        print("Process Terminated")

async def main():
    subfolder_run_files = SUBPROCESS_LIST
    for pair in subfolder_run_files:
        await asyncio.gather(*[run_cmd(x) for x in pair])

asyncio.run(main())
