we create headings in Markdown using hash (#) symbols
To create subheadings, we can use multiple hash symbols
## This is a level 2 subheading

### This is a level 3 subheading

###### This is a level 6 subheading

# Modifying Text Style
we use asterisks to modify text styling, specifically bold
e.g.
I want this **word** specifically to be bold
I want this *word* specifically to be italic
I want this ***word*** to be both bold and italic

## Strikethrough  
ASIDE: If we want to place a character is a *keyword*  or reserved word and we want to LITERAL character, use the forward slash (\\)  
e.g. if we want to put an asterisk we do this \\\*
\*
We can also strikethrough characters using the tilde (~)  
I want to strikethrough this specific ~~word~~  
~~This sentence is struck-through~~

 ~~Strikethrough~~  
We can also strikethrough characters using the tilde (~)  
I want to strikethrough this specific ~~word ~~  
~~This sentence is struckthrough~~

Exercise:
* If you have an openai account, do the following:
	* ask chatgpt to create for you a markdown code that is a link to a website of your choice
* if you don't have openai/chatgpt, create two links to websites of your choice in the space below

e.g. [My favourite website right now](https://nyt.com)

[NOT A RICKROLL](https://www.youtube.com/watch?v=dQw4w9WgXcQ)


e.g. if you use openai
Put in their code, and in italics say that it's from chatgpt
[A search engine](https://google.com) *from chatgpt*

[Click here to get Rickrolled](https://www.youtube.com/watch?v=dQw4w9WgXcQ) *from chatpgt*

**BIG BLACK COCK**
![big black cock](https://i.natgeofe.com/n/2aa7de9d-6e7c-4430-8ef0-003faf6d6a61/01-chicken-breed-black-jr2m68_square.jpg)
# Blockquotes
block quotes allow us to emphasize a bigger chunk of text.
We use carets (\>) to create blockquotes.

>This is an example of a blockquote
>This is line two of the blockquote
>
>This is the fourth line, the third line is blank

# Lists
We can create both unordered and ordered lists
## Unordered Lists
To create each point, we use (\*) with a space behind it
We can create sublists by placing **TABS** before the asterisk

e.g.
* dairy
	* eggs
	* milk
	* cheese
* juice

## Ordered Lists
If there is a specific order to the elements in our list,
we create ordered lists
We use numbers, followed by periods to create ordered lists

e.g.
1. Put butter into mixing bowl
2. Add sugar to butter (*hold shift to get the second line*)
   Add both brown and regular sugar
3. Use the mixer to cream the butter and sugar together

# Tables
We can organize information in tables using Markdown
We can use dashes (\~) and pipes (\|)

Tables in Markdown require headings

e.g.

| Name        | Age        | Sign        | Superpower      |
| ---         | ---        | ---         | ---             |
| Bruce Wayne | 35         | Aquarius    | Intelligence/ $ |
| Mr. Ubial   | Unaging    | All of them | Dad strength    |
| Yourself    | Your age   | Your Sign   | Super strength  |


*The Design Process* is the steps that we take when we create a solution to a problem

There are four steps in our design process
## 1. Design our Algorithm in English (or any human language)
An *algorithm* is a sequence of steps to solve a problem.
In this class, *before* we start ANY programming, we write our steps in English.
## 2. Translate our Algorithm from English to Python
We'll translate our algorithm into "proper" Python.
## 3. Test our Python Algorithm
Check if it works *syntactically*. In other words, we check to see if it BREAKS.
Check if it works *semantically*. In other words, we ask does our algorithm actually solve the problem.
## 4. Share our Work
Once it solves the problem, ship your code to whoever will use it.

`favourite_food` -> name of the variable `=` -> assignment operator `input...` -> value

### [Naming](https://github.com/teacherubial/slss-programming-2023-24/diffs/1?branch=main&commentable=true&commit=c3e93d56cca96fee6543b279d10eb9e209ed3b57&name=main&qualified_name=refs%2Fheads%2Fmain&sha1=1aa1390128f6277f959f4aa10c4d1666c6905d58&sha2=c3e93d56cca96fee6543b279d10eb9e209ed3b57&short_path=acd18ea&unchanged=expanded&w=false#naming)

What you can do:

1. name them with letters, numbers, underscores
2. names **should** start with a lowercase letter What you can't do:
3. you **can't** name them with spaces or symbols
4. you **can't** name them with certain names that are reserved
    1. e.g. `if`, `while`, `for`, `and`, `or`, ...

A good name is something like this:
```python
favourite_food 
fave_food
date_of_birth
student_number
```

Bad names are like this:

```python
Favourite_food
a
num
aa
aaa
aaaa
```

# [Strings](https://github.com/teacherubial/slss-programming-2023-24/diffs/1?branch=main&commentable=true&commit=c3e93d56cca96fee6543b279d10eb9e209ed3b57&name=main&qualified_name=refs%2Fheads%2Fmain&sha1=1aa1390128f6277f959f4aa10c4d1666c6905d58&sha2=c3e93d56cca96fee6543b279d10eb9e209ed3b57&short_path=acd18ea&unchanged=expanded&w=false#strings)

# [Design](https://github.com/_view_fragments/Voltron::CommitFragmentsController/show/teacherubial/slss-programming-2023-24/c3e93d56cca96fee6543b279d10eb9e209ed3b57/commit_show_contents?branch=c3e93d56cca96fee6543b279d10eb9e209ed3b57&qualified_name=c3e93d56cca96fee6543b279d10eb9e209ed3b57&short_path=acd18ea&unchanged=expanded#design)

> Task
> 
> 1. In `input_and_output.py1`
> 2. Put the header
> 3. Write in some comments

## [Input](https://github.com/teacherubial/slss-programming-2023-24/diffs/0?branch=main&commentable=true&commit=1aa1390128f6277f959f4aa10c4d1666c6905d58&name=main&qualified_name=refs%2Fheads%2Fmain&sha1=40241f33718ffbc3b82405ac1d6fc4657a86f5de&sha2=1aa1390128f6277f959f4aa10c4d1666c6905d58&short_path=acd18ea&unchanged=expanded&w=false#input)

We grab information from the user using `input()`.  
When we run the function, it does two things:

1. It **waits** for the user to write something or nothing
2. The user presses **Enter/Return** to indicate that they're finished

```python
input()

input(<prompt>)      # prints out the prompt then waits
```

## [Variables](https://github.com/teacherubial/slss-programming-2023-24/diffs/0?branch=main&commentable=true&commit=1aa1390128f6277f959f4aa10c4d1666c6905d58&name=main&qualified_name=refs%2Fheads%2Fmain&sha1=40241f33718ffbc3b82405ac1d6fc4657a86f5de&sha2=1aa1390128f6277f959f4aa10c4d1666c6905d58&short_path=acd18ea&unchanged=expanded&w=false#variables)

```python
Variables allow us to **store** information for the time that our app is running.

favourite_food = input("What is your favourite food? ")

`favourite_food` -> name of the variable `=` -> assignment operator `input...` -> value
```

# [[Strings]]
