"""python 3.10 implementation of the Elm architectures"""

import asyncio
import json
from enum import IntEnum
import typing as t


# MSG labels
class IncDec(IntEnum):
    Increment = 1
    Decrement = -1


# Model == state
Model: t.TypeAlias = int

# MSG (we defined only 2 possible messages)
MSG = IncDec.Increment | IncDec.Decrement

# the update function updates the model and returns the updated Model
# arguments are the old state and our predefined message
# the return is the new state
Update: t.Callable[[Model, MSG], Model]

# the view function displays state
# in Elm it's HTML
View: t.Callable[[Model], str]

init: Model = 0


async def Update(model: Model, msg: MSG) -> Model:
    match msg:
        case IncDec.Increment:
            return model + 1
        case IncDec.Decrement:
            return model - 1
        case _:
            print('unknown MSG')
            return model


async def View(model: Model) -> str:
    return json.dumps({'model': model})


async def main(init: Model, update: Update, view: View) -> None:
    await View(init)
    model = await Update(init, IncDec.Increment)
    await View(model)


if __name__ == "__main__":
    asyncio.run(main(init=init, update=Update, view=View))
