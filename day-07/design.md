<h1>Day 07 – Thinking Before Coding (DevOps Mindset)</h1>

<h3>Script:</h3>
<p>
  <ul>
    <li>If we look back to our previous work, we have completed different tasks which involves different approaches to write a script which is used to Automate a simple task.</li>
    <li>For this task we are going to answer few questions which builds a mindset with which a devops engineer should approach a script writting.</li>
    <li>There if we take a example for day-06 task which was to convert the log_analyzer python script into CLI tool.</li>
  </ul>
</p>

<h3>Q1. What is the problem?</h3>
<p>
  <ul>
    <li>The existing OOPs Log_analyzer cannot be used like professional CLI tool.</li>
    <li>This requires manual modification to the script to change which log file to read, where to save result.</li>
    <li>Because of this the script is not portable, automation-friendly.</li>
  </ul>
</p>

<h3>Q2. What input does it need?</h3>
<p>
  <ul>
    This requires-
    <li>One log file as input</li>
    <li>One .txt or .json file to save output</li>
    <li>Bonus: we can give which level it should analyze for (ex. ERROR, INFO, WARNING)</li>
  </ul>
</p>

<h3>Q3. What output should it give?</h3>
<p>
  <ul>
    It should-
    <li>It should print a counts of logs.</li>
    <li>It should print result of the logs count to a .json or .txt file.</li>
  </ul>
</p>

<h3>Q4. What steps are involved?</h3>
<p>
  <ul>
    <li>Import the required modules for the script (argparse and json).</li>
    <li>Create a class which involves various methods.</li>
    <li>write a function which read logs from the log file.</li>
    <li>function which analyze the logs and make the count 0 first</li>
    <li>function which write the output to the json file directly if no input is given by the user</li>
    <li>write main() function which adds the arguemnt using agparse and create object to process the logs</li>
  </ul>
</p>
