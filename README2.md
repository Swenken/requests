# Report for Assignment 1 resit

## Project chosen

Name: <requests>

URL: <https://github.com/psf/requests>

Number of lines of code and the tool used to count it: <7560, lizard>

Programming language: <Python>

## Coverage measurement with existing tool

<Inform the name of the existing tool that was executed and how it was executed>
The name of the tool used: Coverage.py
Usage: First it needed to be installed with : pip install coverage
Then run the tests with coverage it in the desired directory : coverage run -m pytest
Lastly to see the report: coverage report
<Show the coverage results provided by the existing tool with a screenshot>

## Coverage improvement

### Individual tests

<The following is supposed to be repeated for each function (2 in total)>

<Function 1> compat_module.py
https://github.com/psf/requests/compare/main...Swenken:requests:main#diff-432ec46da784295df1dae523c21e6dae953e416bdd0374bfb903226239126b7b
<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced tests for function 1>

<Provide a screenshot of the old coverage results for such function>

<Provide a screenshot of the new coverage results for such function>

<State the coverage improvement with a number and elaborate on why the coverage is improved>
Coverage Improvement: 50% → 100%
Reason for Improvement: The coverage improved because the enhanced test (test_u_function) was designed specifically to cover the functionality of the u function in compat.py. The previous tests were not comprehensive enough to cover all scenarios, resulting in lower coverage. The new tests include cases that were previously missed, ensuring that all lines and branches of the u function are now tested, leading to 100% coverage.
<Function2> misc.py
https://github.com/psf/requests/compare/main...Swenken:requests:main#diff-432ec46da784295df1dae523c21e6dae953e416bdd0374bfb903226239126b7b

Coverage Improvement: Improved coverage percentages across affected files.
Reason for Improvement: By adding new tests and enhancing existing ones in misc.py, the coverage is improved because more lines of code and edge cases are now covered. This ensures that potential bugs or unhandled scenarios are identified and addressed, leading to more robust and reliable code.
### Overall

<Provide a screenshot of the old coverage results by running an existing tool (the same as you already showed at the beginning of the report)>
Overall Percentage Unchanged: The overall coverage percentage remains at 47%. This indicates that while some files may have seen improvements in coverage, others either stayed the same or possibly saw a decrease, resulting in no net change in the overall coverage percentage.

Enhancements and Impact: Despite individual improvements in specific tests or functions (such as the ones we discussed), the overall percentage may not have moved due to several reasons:

The enhancements might have focused on specific areas that were previously poorly covered, improving those areas but not affecting the entire codebase.
There might be large portions of code that were not touched by the recent enhancements, thus their coverage status remained unchanged.
Any improvements in coverage were offset by areas where coverage decreased due to changes or removal of tests.
<Provide a screenshot of the new coverage results by running the existing tool using all test modifications>
