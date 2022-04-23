import adagio

async def identity(value):
    return value

async def print_evens(group=None):
    for i in range(0, 6, 2):
        print(await identity(i))
        await adagio.sleep(.25)
    if group:
        group.schedule(print_odds())
    else:
        with adagio.Group() as g:
            g.schedule(print_odds())

async def print_odds():
    for i in range(1, 11, 2):
        print(i)
        await adagio.sleep(.25)

print("groups:")
with adagio.Group() as g:
    g.schedule(print_evens(group=g))
    g.schedule(print_odds())

print("await from sync context:")
adagio.a_wait(print_odds())
