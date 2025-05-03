import time 
import asyncio


async def print_numbers():
    for i in range(5):
        print(i)
        # await time.sleep(1) which is a blocking (synchronous) 
        # function, inside an async function, and trying to await
        # it — but time.sleep() is not awaitable.
        await asyncio.sleep(1) #is the non-blocking, asynchronous version of time.sleep()
asyncio.run(print_numbers())