# startup
simple gui to start programs,

i probably won't work on this any more unless i'm really bored

## how to add programs:

optionally, you could edit the 4 pre-written code thats already avaliable for ease, but this will teach you how to add more manually.

1. below lines 9-12 (`self.var1-4=IntVar()`), add your own name, or follow the pattern. for example:

`self.var5=IntVar()`

or

`self.dlkjh=IntVar()`

just remember to type dlkjh correctly, you'll need it later.

2. next, below lines 18-25 (placeholder stuff), add your own name yet again

`name = Checkbutton (self, text="title", variable=self.var5`(or self.dlkjh)`, onvalue=1, offvalue=0)`

`name.place(x=somewhere, y=somewhere)`

cool ! you're almost done

3. now in ```def startSelected``` you need to write a few lines of code for it to work:
```
if(self.var5.get() == 1):
    os.startfile('"path"')
elif(self.var5.get() == 0):
    pass
```
now you're done

## important
specifying path is quite confusing sometimes, heres how to do it right:
the single quotes (') are what python reads, the double quotes (") is what ~~shitdows~~ windows will read.
to actually write a path, here's an example and you can fill in the blanks:

`'"C://Users/`yourusername`/`path`/program.exe"'`

## also important
near the bottom of the python file (line 60 (root.geometry("220x120")), you can simply change the numbers to something bigger if you have to in order for more to fit

### known issues
opening cmd will freeze the gui
opening some programs like discord will also open a command prompt which will also close discord if you close the command prompt
