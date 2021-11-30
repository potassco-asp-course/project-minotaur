# Minotaur Project

You can find the instructions of the project in the file [minotaur.ipynb](minotaur.ipynb).

To submit your solution, please modify the file [minotaur.lp](asp/minotaur.lp) of the directory [asp](asp) with your encoding.

Every time you push a new commit, your solution will be tested automatically.
The timeout per instance is `300` seconds, and
the actual command call for the test is:
* ``python3.6 asp/test.py asp/minotaur.lp 300 OPT``

Your encoding has to find *one* optimal solution of the problem. This is what the script `test.py` checks.

After a few minutes you will be able to see the result of the test in the **Actions** tab.
You can get more information about the result of the test by clicking successively on:
1. The specific test.
2. "Autograding".
3. "Run education/autograding@v1".

Then scroll down until around line 150.
For each instance, you will see if the test is a:
* "success" (correct answer),
* "failure" (wrong answer),
* "timeout" (no solution found before the time runs out), or
* "error" (clingo error).
