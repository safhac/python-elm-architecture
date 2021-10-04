"""python 3.10 implementation of the Elm architectures"""

"""
in Elm everything is a function
and every function must return a value


the elm architecture has 4 basic components:

[Model] 
represents the 'state' so it's a function that returns state

[Update]
a function that updates the Model or state
the arguments are the old model and the message and the return type is Model
def Update(model: Mode, msg: MSG) -> Model:
    ...

[MSG]
the message - elm creates types to represent message
so imagine creating a class to represent an event in the program

 
[View]
a function that displays the state [Model] - in Elm it's HTML
def View(model: Model) -> Html[Model]:
    ...

[init]
since in Elm there are no null or undefined
the init function creates the initial state
init: Model = 0   
"""
import asyncio
import json
import typing as t

# MSG labels
Increment: t.Callable[[...], int] = 1
Decrement: t.Callable[[...], int] = -1

# Model == state
Model: int = 0

# MSG (we defined only 2 possible messages)
MSG = Increment | Decrement

# the update function updates the model and returns the updated Model
# arguments are the old state and our predefined message
# the return is the new state
Update: t.Callable[[Model, MSG], int]

# the view function displays state
# in Elm it's HTML
View: t.Callable[[Model], str]

init: Model = 0


async def Update(model: Model, msg: MSG) -> Model:
    match msg:
        case 1:
            return model + 1
        case -1:
            return model - 1
        case _:
            print('unknown MSG')
            return model


async def View(model: Model) -> str:
    return json.dumps({'model': model})


async def main(init: Model, update: Update, view: View) -> None:
    await View(init)
    model = await Update(init, Increment)
    await View(model)


if __name__ == "__main__":
    asyncio.run(main(init=init, update=Update, view=View))
