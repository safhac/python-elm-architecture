# Python Elm architecture

### in Elm everything is a function and every function must return a value


## the elm architecture has 4 basic components:

[Model] 
- represents the 'state' so it's a function that returns state

[Update]
- a function that updates the Model or state
the arguments are the old model and the message and the return type is Model
def Update(model: Mode, msg: MSG) -> Model:
    ...

[MSG]
- the message - elm creates types to represent message
so imagine creating a class to represent an event in the program

 
[View]
- a function that displays the state [Model] - in Elm it's HTML
def View(model: Model) -> Html[Model]:
    ...

[init]
- since in Elm there are no null or undefined
the init function creates the initial state
init: Model = 0   

