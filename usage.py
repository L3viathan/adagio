import adagio

async def identity(value):
    return value

async def print_evens():
    for i in range(0, 10, 2):
        print(await identity(i))
        await adagio.sleep(1)

async def print_odds():
    for i in range(1, 11, 2):
        print(i)
        await adagio.sleep(1)

async def main():
    adagio.schedule(print_evens())
    adagio.schedule(print_odds())

adagio.run(main)

# adagio.a_wait(print_evens())
