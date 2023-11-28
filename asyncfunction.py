import asyncio


async def sub():
    print('starting the sub function')
    await asyncio.sleep(2) # asyncio.sleep(2) instructs the event loop to pause the execution of the sub function for one second before continuing.
    print('ending the sub function')


async def main():
    print('starting exection of the main function')
    await sub()
    # The await sub() call indicates that the function is awaiting the completion of the sub function before continuing.
    print('ending the main function')

asyncio.run(main())
# The asyncio.run(main()) statement starts an event loop and executes the main function.
# The event loop manages the execution of asynchronous tasks, including the sub function, which is called from the main function.




# An asynchronous function in Python is a function that allows the execution 
# of other code while it is waiting for an I/O operation to complete.
# This is in contrast to a synchronous function, which blocks the execution of the program until the I/O operation is finished.


# Asynchronous functions are particularly useful for network programming and other I/O-bound tasks,
# where the time it takes to complete an operation can vary significantly.
# By using asynchronous functions, you can prevent your program from blocking while waiting for these operations to finish,
# allowing it to handle other tasks in the meantime.


# To use asynchronous functions in Python, you need to use the async and await keywords.
# The async keyword is used to define an asynchronous function, 
# while the await keyword is used to wait for an asynchronous operation to complete
