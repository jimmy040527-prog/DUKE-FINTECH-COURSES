# History Currency Conversion

This assignment provides you with practice in working through the initial steps
of the [Seven Steps](https://fintechpython.pages.oit.duke.edu/jupyternotebooks/1-Core%20Python/02-ProblemSolvingByProgramming.html).  
Focus on creating the initial algorithm and how you can test that it works 
correctly.

You'll also use [Markdown](https://www.markdownguide.org/) to provide your 
answer. We'll use Markdown as the source for all of the programming assignment
descriptions.  You will also use it throughout 510 and 512 to create documentation.
More importantly, you'll see that it has become one of the most common formats used
by developers. [Basic Syntax] covers the initial syntax you'll need for this
assignment. You can preview Markdown within VS Code by 
typing Ctrl-Shift-V on Windows or Command-Shift-V on macOS.

## Problem
As part of a financial system, we'll need to convert between different currencies 
and analyze how exchange rates have changed over time.  Assume that the system
tracks available currencies (e.g., U.S. Dollar ($), the Euro (€), 
the Renminbi/Chinese Yuan(¥), etc.).  You'll need to ask the user 
for the source currency, target currency, amount to convert, and the
historical day to consider (e.g., November 8th, 2012).  The system
will perform the conversions for the historical date as well as the
current date, displaying the converted amounts. You'll also need to display
whether the target currency has gained or lost in purchasing power and
by what percentage.

## Assignment Details
1. Write an algorithm to enter the necessary information, perform the conversions,
   determine if the currency has gained or lost purchasing power, and by what
   percentage. 
2. Write four possible test cases that you can use to test your generalized
   algorithm. Consider both the "normal" path, where the system would work
   as expected, and error conditions/paths. What would happen if a currency 
   did not exist?  What happens with extreme amounts (both large and small)?
   What if the amount was negative?

3. In a file called `answer.md`, place the following information:
   1. A top-level heading (level 1) with a label of "Historical Currency Conversion"
   2. An optional description under that heading
   3. A second-level heading (level 2) with a label of "Algorithm"
   4. List at least 3 steps as an [ordered list](https://www.markdownguide.org/basic-syntax/#ordered-lists)
   5. Another second-level heading (level 2) with a label of "Tests"
   6. Describe at least 4 possible test cases as an unordered list

4. Submit `answer.md` for grading in Gradescope.
