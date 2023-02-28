<table><tr><td> <em>Assignment: </em> M4-Simple-Calc</td></tr>
<tr><td> <em>Student: </em> Praneeth Ravella (pr457)</td></tr>
<tr><td> <em>Generated: </em> 2/27/2023 11:26:22 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/m4-simple-calc/grade/pr457" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p>Make sure you're working in an up to date branch</p><ul><li><code>git checkout dev</code></li><li><code>git pull origin dev</code></li><li><code>git checkout -b M4-Simple-Calc</code></li></ul><p>This will likely be started in class.</p><p>Steps:</p><ol><li>Create a new Folder called M4</li><li>Create a new file called MyCalc.py inside this folder</li><li>Create a MyCalc Class</li><li>Define basic addition / subtraction / multiplication / division functions<ol><li>These functions should update an internal variable as a running total/value called&nbsp;<code><b>ans</b></code></li><li>All functions must properly handle the math given standard math scenarios (i.e., show proper messages when trying to divide by zero for example)</li><li>Since you'll likely be taking screenshots of the code, make sure you add a comment with your ucid and the date</li></ol></li><li>Define a "main" logic to run when the program runs</li><li>This logic should ask for user input<ol><li>The input can be any valid number, any valid math operator, and any valid number (i.e., 2 * 2)<ol><li>This will do an immediate calculation, print it, and store the answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li><li>Alternatively, the input can be&nbsp;<code>ans</code>, any valid math operator, any valid number (i.e.,&nbsp;<code>ans</code>&nbsp;* 2)<ol><li>This will use the previous answer (or 0 if not set) as part of the calculation, print it, and will store the new answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li></ol></li><li>Create a test case for each scenario that utilize functions to have expected input and compare against expected output, all cases should pass (test cases should have a series of data passed into them)<ol><li>Test number-add-number</li><li>Test ans-add-number</li><li>Test number-sub-number</li><li>Test ans-sum-number</li><li>Test number-mult-number</li><li>Test ans-mult-number</li><li>Test number-div-number</li><li>Test ans-div-number</li></ol></li><li>Create a new file called m4_submission.md inside the M4 folder</li><li>Fill out the below deliverables</li><li>Generate the markdown and paste it into the m4_submission.md</li><li><code>git add .</code></li><li><code>git commit -m "adding m4 hw"</code></li><li><code>git push origin M4-Simple-Calc</code></li><li>Create a pull request M4-Simple-Calc to dev</li><li>Create a pull request dev to prod (after the previous one is merged)</li><li>Navigate to the prod branch on github, go to the M4 folder, click the m4_submission.md</li><li>Submit this link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Snippets (Make sure each screenshot has a comment showing your ucid and the date it was written) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of valid Addition Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/221747425-7be72fa3-3b43-4cde-be7d-b3597b1bd51d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of valid Addition Function with ucid, date, and brief description/summary<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/221747611-1552edb4-bada-4ee5-ab0d-ca599dc093b8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of addition function output<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/221747724-3e528a60-f349-4888-9cc2-581516684cca.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of utility functions _is_float, _is_int and _as_number<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of valid Subtraction Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/221747936-5990862a-41c8-4b2d-8a11-113160f1b023.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of valid Subtraction Function with ucid, date, and brief description/summary<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/221748058-7e0fe6b2-6eb4-44b2-82d8-07f30ca14752.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Subtraction function output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of valid Multiplication Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/221748248-f2c58126-1a6e-4103-8abd-d437aa70e929.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of valid multiplication Function with ucid, date, and brief description/summary<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/221748400-e77b63ba-f02f-45e3-a495-4adc8039391d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of multiplication function output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of valid division Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/221748582-bd0f2150-dfa6-4aed-bb46-15ae607ac98f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of valid division Function with ucid, date, and brief description/summary<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/221748766-5ae2d98e-95e1-4a55-8ed3-ab03d0c86256.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of division function output and handling of the divide by zero error<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Test Case Validations </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of passing number-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/221749055-bfc00f6a-ff6c-4397-bfda-676f97452597.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the fixture containing data for num-op-num test case<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/221749592-e656956e-1eca-4336-8421-cf23ed9d60f4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the test case code with Comment containing ucid, date, and brief<br>description/summary<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/221750877-920d2d7d-3af2-4c66-af07-b6af5fb16d27.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of test case passing in pytest<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of passing ans-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/221749327-4170dd14-9aba-4e92-951f-84a94dcafe4b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the fixture containing data for ans-op-num test case<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/221749720-a967063e-3f61-4fbe-8cac-254f4c78eb86.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the test case code with Comment containing ucid, date, and brief<br>description/summary<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/221751037-dd8f62c2-5445-4e35-8a62-c78c03411a4e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of test case passing in pytest<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of passing number-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/221749055-bfc00f6a-ff6c-4397-bfda-676f97452597.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the fixture containing data for num-op-num test case<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/221749847-0f62f479-e86c-4d0d-a667-6c0312585902.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the test case code with Comment containing ucid, date, and brief<br>description/summary<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/221751236-7eda0945-c225-49ad-aabd-465a49ec27b2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of test case passing in pytest<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshots of passing ans-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/221749327-4170dd14-9aba-4e92-951f-84a94dcafe4b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the fixture containing data for ans-op-num test case<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/221749922-18336bab-ebb2-4c6b-8903-c3d5ab5f0a28.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the test case code with Comment containing ucid, date, and brief<br>description/summary<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/221751424-0322cf38-b7f2-4367-8abf-453bf97e6740.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of test case passing in pytest<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Screenshots of passing number-mult-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/221749055-bfc00f6a-ff6c-4397-bfda-676f97452597.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the fixture containing data for num-op-num test case<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/221750018-a3bee307-09da-4856-9ccb-4facb985c7ca.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the test case code with Comment containing ucid, date, and brief<br>description/summary<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/221751534-8c79dab2-fbfd-425d-927f-3fb8969f042c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of test case passing in pytest<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Screenshots of passing ans-multi-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/221749327-4170dd14-9aba-4e92-951f-84a94dcafe4b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the fixture containing data for ans-op-num test case<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/221750088-f893edcf-ec33-4a10-801e-9f37ea2eb720.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the test case code with Comment containing ucid, date, and brief<br>description/summary<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/221751688-d9cb135d-b7fc-4376-b06f-f85188e76a1d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of test case passing in pytest<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Screenshots of passing number-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/221749055-bfc00f6a-ff6c-4397-bfda-676f97452597.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the fixture containing data for num-op-num test case<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/221750173-f35be6e1-cdcf-4dfa-bf9c-15680af536b7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the test case code with Comment containing ucid, date, and brief<br>description/summary<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/221751804-b8bd0280-978a-4fc5-a40e-f4db120d7db8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of test case passing in pytest<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 8: </em> Screenshots of passing ans-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/221749327-4170dd14-9aba-4e92-951f-84a94dcafe4b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the fixture containing data for ans-op-num test case<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/221750243-0aa20a19-387c-4305-8b3c-6bf11cf67b37.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the test case code with Comment containing ucid, date, and brief<br>description/summary<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/221751899-15a15962-003c-422f-bef2-3ad68e256899.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of test case passing in pytest<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Briefly talk about anything you learn during this assignment/module</td></tr>
<tr><td> <em>Response:</em> <ol><br><li>How the test cases are designed<div>2) How fixtures can help in providing<br>the data for test cases</div><div>3) How comparison of the floating point numbers works</div><br></li><br></ol><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Discuss how test cases work and anything new you learned about them while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <ol><br><li>Test cases are used to verify if the program is working as<br>intended.&nbsp;When a test case is executed, the testing framework (pytest in this case)<br>will run the code associated with the test and compare its output to<br>an expected result. If the output matches the expected result, the test case<br>passes. If not, the test case fails, indicating that there may be a<br>problem with the code being tested. Test cases can be automated to make<br>testing more efficient and reliable<div>2)&nbsp;Unit tests serve as the foundation for developing software<br>with fewer unexpected errors and improved efficiency. By testing individual components or functions<br>of the system, unit tests help to identify bugs early in the development<br>process and ensure that each component behaves as expected. Also when adding a<br>new feature, unit test cases can be run to make sure that no<br>existing functionality is broken due to the new features.</div><br></li><br></ol><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the pull request of M4-Simple-Calc to Dev link</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/ravella10/IS601-006/pull/7">https://github.com/ravella10/IS601-006/pull/7</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/m4-simple-calc/grade/pr457" target="_blank">Grading</a></td></tr></table>