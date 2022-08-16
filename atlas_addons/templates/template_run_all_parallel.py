import os
import asyncio

async def run_cmd(cmd):
    os.system('python '+cmd)

async def main():
    subfolder_run_files = SUBPROCESS_LIST
    tasks = []
    for cmd in subfolder_run_files:
        task = asyncio.create_task(run_cmd(cmd))
        tasks.append(task)

    for task in tasks:
        await task

asyncio.run(main())
