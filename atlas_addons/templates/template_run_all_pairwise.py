import os
import asyncio

async def run_cmd(cmd):
    try:
        proc = await asyncio.create_subprocess_shell(
            "python "+cmd,
            shell=True,
            stdout=asyncio.subprocess.DEVNULL,
            stderr=asyncio.subprocess.DEVNULL)
        await proc.communicate()
    except asyncio.CancelledError:
        proc.terminate()
        print("Process Terminated")

async def main():
    subfolder_run_files = SUBPROCESS_LIST
    for pair in subfolder_run_files:
        await asyncio.gather(*[run_cmd(x) for x in pair])

asyncio.run(main())
