# Project: Graph Theory 2021
**Name:** Emmanuel Osabuehien
**Student ID:** G00373559
**Module:** Graph Theory

## What is a regular expression?

 Before we get into what is a regular expession in python, the whole concept and development of a regular expression can be dated back to as early as the 1950's and maybe even in the 1940's but in 1951, the concept of regular language was created by a mathematician by the name of Stephen Cole Kleene, where we have a language that can be idenitfied by a finite automaton and represented using regular expression.

As we move on to the 1960's where a Ken Thompson who was a computer science pioneer and is also one of the designers of Unix (a multitasking, multiuser computing operating system) would add the concept of matching patterns in a text editor using Stephen Cole Kleene's code and in the 1970's is when we really see regular expressions takeover the programming world, another note is the whole concept became common use with Unix text-processing.
 
As we move on to modern day computer science, we see how highley influential this was as we now see the use of regular expressions in so many different programming languages such as Python, C#, Javascript and many more but also regular expressions are used in text editor as well as a use for other tools where we can regulate if a special sequence of characters or string match a specific pattern.

Now we move on to the main question what is a regular expression, A regular expression or sometimes referred to as a regex can be defined as a unique set or sequence of characters that are used to to match, locate and manage a set of strings.

Here is an example of using regular expression in python for pattern matching:

s = 'emmanuel70156'

import re

if re.search('123', s):
    print('Found a match.')
else:
    print('No match.')

As you can see in the above code, the regex is '015' and the string is 's' and re.search is used to return the match object instead of null and when it is run in python it should print out the text 'Found a match.'

One of the most common methods of using a regular expression is used in a command line and in text editors to find text inside a file and another use is when search engines use regular expression to search and replace dialogs of word processors and text editors.

Perl is one good example of a prograaming language that uses regular expression as this arose in the 1980's and it was originally fored from regular expression library and this library was later expanded and added many new features.

An example of using regular expression in Perl could be as follows:

$data =~ s/e/E/;

The above example is a piece of code where we search and replace any data variable with a lowercase 'e' with and uppercase 'E', e.g. 'An elephant in the river' gets replaced with 'An ElEphant in the rivEr'.

We can even change this to change a whole world for example:

$data =~ s/happy morning/good night/i;

The above example is a piece of code where any data variable wih 'happy morning' changes to 'good night', e.g. 'Have a happy morning' changes to 'Have a good night'.

So this all here is all about regular expressions from a brief history of the concept and creation, to it's impact in programming languages, to some examples of it's uses and most important the definition of what is a regular expression.

 ## How do regular expressions differ across implementations?

 

 ## Can all formal languages be encoded as regular expressions?

When I was talking in the previous question (What is a regular expression?), I made some references to how there are many different programming languages that use regular expression "we see how highley influential this was as we now see the use of regular expressions in so many different programming languages such as Python, C#, Javascript and many more but also regular expressions" and as I continue you will see me dig a bit deeper with my answer to this question but before that let me give you some details about formal languages in the context of regular expressions.

We know we can use regular expression (regex) in languages such as Python and Javascript but if we step out of those languages and use this same approach then can we expect the same results to be produced.

Now most of us like to copy and paste to save time and comfort but can we use this same method across all different programming languages and can all programming languages accept this.

Every regular expression denotes a formal language but a formal language is only regular if there is a regular expression denoting it.

While programming languages are composed of a syntax representing program as strings and characters and is the meaning of the program and on the other hand a formal language are syntaxes without any meaning and is used to study the structure of a set of strings defined formally without attaching meaning to those set of strings.

So as I move on with my answer to this question, can all formal languages be encoded as a regular expression, to break it down easy and simply in layman's terms I will say that most formal languages can be encoded as a regular expression.

This all ties in with the concept of a regular language, a regular language that can be defined by a regular expression.

There are many reasons why most formal languages can use regular expressions while some can't, one of the reasons that not all formal languages can be encoded using regular expressions is as simple as not all languages support the same features which means for language such as the aforementioned PERl using this type of code is perfectly fine while in some other languages it may completely unreadable and impossible to debug.

Some languages may use the same syntax for different features and even for the same features but they can also exhibit different behaviour which makes it hard to reuse the regular expressions across different formal languages.

So long story short, technically no not all formal languages can be encoded as regular expressions for many reasons while there are a lot of languages that use regular expressio there is also many that don't for many reasons.

For this question in general if you have more questions about it I suggest you read this document which I found very helpful in discussing this question:

[*Why Aren't Regular Expressions a Lingua Franca?*, An Empirical Study on the Re-use and Portability of Regular Expressions,<br> https://people.cs.vt.edu/~davisjam/downloads/publications/DavisMichaelCoghlanServantLee-LinguaFranca-ESECFSE19.pdf/](https://people.cs.vt.edu/~davisjam/downloads/publications/DavisMichaelCoghlanServantLee-LinguaFranca-ESECFSE19.pdf/)

 ## References

 Here is a list of references that helped me with the research of my project:

 1. [*Why Aren't Regular Expressions a Lingua Franca?*, An Empirical Study on the Re-use and Portability of Regular Expressions,<br> https://people.cs.vt.edu/~davisjam/downloads/publications/DavisMichaelCoghlanServantLee-LinguaFranca-ESECFSE19.pdf/](https://people.cs.vt.edu/~davisjam/downloads/publications/DavisMichaelCoghlanServantLee-LinguaFranca-ESECFSE19.pdf/)