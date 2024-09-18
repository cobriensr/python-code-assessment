# Beam's Python Kata
Beam is a data driven company, and therefore works to explore a lot of tables and data sets that we both generate and receive.
This kata aims to emulate that reality, through the analysis of car purchase data. 

This kata involves intaking a csv file, breaking it apart, running through a series of specific queries, and printing out the answers into a console.
The focus should be on accurately reading and manipulating the data so that each question is answered precisely.

## Instructions
---
Please read through each of the questions below and implement the functionality to answer them according to their requirements.
The code design is entirely up to you as long as the solution can be run via a python3 command (see [Additional Sections](#additional-sections)). We also ask that you commit your work to git frequently as you go.

### Evaluation Criteria
As there are often trade-offs when crafting a solution, the following is the priority of what we are considering when reviewing your kata:

* Functionality: The solution should fulfill the requirements and work correctly. Please feel free to reach out if you have questions about the provided user stories.
* Testing: Beam firmly believes in testing as a practice and as such we ask that you add tests. While the choice of testing tools is left up to you, we prefer to see code that has good test coverage.
* Structure: Well-factored code is easier to reason about and maintain. We prefer to see good separation of concerns in the architecture.
* Idiomatic code: Along similar lines, code that adopts the best practices, idiom and conventions of the language/framework helps with readability and maintainability.

### Additional Sections
These sections will help us understand your thought process and workflow while we review your solution. Feel free to add these sections to this README or in a separate file.

* Technical decision making: Please add a section explaining the technical decision making involved in designing your solution. What options were you considering at various levels (eg. tech stack choice, libraries, and design, as applicable) and what were the trade-offs in choosing one option over another?
* Instructions on running your code: As you decide on the tools to build the solution, please add a section letting us know how to run your code and tests.

## Submitting your work to Beam
---
For ease of evaluation, we require that this kata is completed using python 3.10 or above.

Once you're happy with your submission (evaluation criteria, additional sections), you can send it back as a zip file.

To ensure that our review of your kata remains as unbiased as possible, your submission will be anonymized before it is reviewed.
To help us with this process, please double check that any personally identifiable information, such as your name or email address, is removed from your code, README or any commit messages.
Your author and committer information will be scrubbed by our anonymizing process.

## Questions to Answer
---
Navigate to this [dataset](https://docs.google.com/spreadsheets/d/1CAQJlbQBrIrKYCCNQFMeIG2u8BAuDjHfIje_07zDqvQ/edit?usp=sharing) and click File -> Download -> Comma-separated Values (CSV) to download the csv version. Ensure that the csv filename is `car_sales_dataset.csv`.

In order to keep the repository small, we ask that you don't commit the data set to the repository.  In your README instructions, please note where the file should be downloaded.

Three questions/prompts need to be answered based off of the data provided:

* Give the average and median difference in the Sale vs Resell price for all buyers in a zip code whose first two digits are in the range 00-19 (each naturally/arithmetically rounded to 2 decimal places.)

e.g.
```bash
  Price Differences: 
  Average: $123.45 | Median: $100.01
```

* Print the date and sales price of all Porsche owners 3 years after initial purchase date using the annual depreciation rate (with calculated amount naturally/arithmetically rounded to 2 decimal places.) 

Note: All dates will be after 1940 up to present day.

The equation to calculate depreciation is

```math
                t 
A(t) = A'(1 - r)    , where A' is the initial purchase price, r is the depreciation rate, and t is the time in years.
```


e.g.
```bash
  Purchase Date  |   Depreciated Value
  1950-09-09     |   $12345.67
  1970-10-10     |   $13579.13
  2010-11-11     |   $12468.02
  ...
```

* Print the 10 highest ratios of the sales price of used cars compared to their top speed (please have the ratio naturally/arithmetically rounded to 3 decimal places.)

e.g.
 ```bash
  Sales Price  |  Top Speed  |  Ratio
  $81253.92    |  200.9      |  404.449
  ...
```

While there's freedom in the UI, we ask that it's command line centric with a good explanation of usage.  The focus of this kata is more on the quality of the code, its architecture, and the accuracy of the answers.

## Running your code
We have purposefully not written instructions on how we will run both your main program or your test suite.
This is to give you a chance to show us how you would structure a project like this.
Because of this, we ask that you include detailed instructions on how to both run your code and its test suite, and preferably which directory to run them from.