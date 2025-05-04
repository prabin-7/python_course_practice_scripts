import time 
import asyncio


async def print_numbers():
    for i in range(0,5,2):
        print(i)
        # await time.sleep(1) which is a blocking (synchronous) 
        # function, inside an async function, and trying to await
        # it — but time.sleep() is not awaitable.
        await asyncio.sleep(1) #is the non-blocking, asynchronous version of time.sleep()
async def try_gar(name: str):
    print(f" Task {name} started ....")
    for i in range(5):
        print(i)
        await asyncio.sleep(0.5)
    print(f"Task {name} completed!")

async def  main():
    # task = asyncio.create_task(print_numbers())
    # await task
    start = time.perf_counter()
    await asyncio.gather(try_gar('task#1'),
                         try_gar('task#2'),try_gar('task#3'),
                         try_gar('task#4'),)
    print(f"end time is : {time.perf_counter() - start}")
if __name__ == "__main__":
    # asyncio.run(print_numbers())
    asyncio.run(main())
    # main()            # this returns only a coroutine object

# async def try_gar(name: str):
#     print(f"Task {name} started .....")
#     await asyncio.sleep(0.5)
#     print(f"Task {name} finished!")

#async fxn chalauna lai asyncio.run(task())
#asyncio.gather