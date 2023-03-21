<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 2 - Burgers</td></tr>
<tr><td> <em>Student: </em> Praneeth Ravella (pr457)</td></tr>
<tr><td> <em>Generated: </em> 3/20/2023 11:39:12 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-2-burgers/grade/pr457" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Create a new branch per the desired branch name below</li><li>Add the baseline files from the following link:&nbsp;<a href="https://gist.github.com/MattToegel/028db0e3fd2b20c1fb8e284b341292bb">https://gist.github.com/MattToegel/028db0e3fd2b20c1fb8e284b341292bb</a>&nbsp;</li><li>Put them into a subfolder in your repository folder (I called my folder BurgerMachine)</li><li>git add .</li><li>git commit -m "baseline files"</li><li>git push origin (name of desired branch below)</li><li>You can go to github and open the pull request for evidence capturing later (don't close/merge the pull request until you're done with the assignment)</li><li>Do the below tasks and fill in the below entries</li><ol><li>git add/commit after any significant changes to build up history</li></ol><li>Save the input and generate the submission markdown file (copy to clipboard or download the file)</li><li>Name it something relevant to the assignment if it's not named already</li><li>git add the submission file</li><li>git commit the submission file</li><li>git push the submission file</li><li>Complete the pull request to dev</li><li>Create a pull request from dev to prod</li><li>Go to the prod branch on github, navigate to the submission file</li><li>Paste that link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Changes - Add the calculate_cost() implementation </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of the updated method calculate_cost()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/226509757-b9bc701b-102e-4474-b54a-371ee9f86d70.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of calculate_cost() which includes comment with ucid and date, logic to calculate<br>the proper value of the inprogress_burger array and return that value from the<br>function<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/226509805-6d80f5f6-700c-46ad-8843-885ec558bf0a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of input() message displaying the value in currency format<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/226497319-925ce64a-3fed-4287-b8b1-fdf6406685cc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of output message displaying the value in currency format and asking total<br>to be entered as currency format<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain the approach to implementing the calculation</td></tr>
<tr><td> <em>Response:</em> <p>1)cost is calculated by iterating through all usables in the inprogress_burger list and<br>adding them up<br>2) currency formatting is handled by format() method to format the<br>float value with the &#39;{:,.2f}&#39; format specifier and then converts it to a<br>float using the float() method.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Exception Handling </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of adjusted code to handle exceptions</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/226499311-9d3add00-9d6f-4ffd-9e34-cd9d9a487a6b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of OutOfStockException handled with proper user feedback and continued program flow. Shows<br>the stage/category that the choice was out of stock in<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/226499683-e6a1b2b7-65ee-4799-9bf0-40d17a93c530.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of how the NeedsCleaningException is handled where it prompts the user to<br>type the word &#39;clean&#39; to clean the machine; other words are ignored. Prints<br>a message whether or not the machine was cleaned.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/226499861-974c1c4a-ddf8-4b6f-892f-219358cbbc4f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of how the various InvalidChoiceExceptions are handled with proper user feedback and<br>continued program flow. Shows the stage/category that the choice was invalid in<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/226500188-a9e71a67-883f-46f1-ae7f-42e90d290d1a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of how the various ExceededRemainingChoicesExceptions are handled with proper user feedback and<br>continued program flow. Shows the stage/category where the choice limit was exceeded. Moves<br>the user to the next stage/category<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/226500762-f0365cc0-9a64-46c2-bf4c-1ab35fbc143d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of how the InvalidPaymentException is handled with proper user feedback and continued<br>program flow<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each exception handling process</td></tr>
<tr><td> <em>Response:</em> <ol><br><li>OutOfStockException is handled by checking the most recent selection which in inprogress_burger<br>list and displaying it&#39;s category name along with usable name and giving user<br>a chance to select something else<br>2)&nbsp;<span style="font-size: 13px;">NeedsCleaningException&nbsp;is handled by asking user to<br>enter the command &#39;clean&#39; and check if the command given matches, if it<br>does then&nbsp;clean_machine function is invoked and success message is displayed or else failure<br>message displayed and the same stage contiues<br>3)&nbsp;</span><span style="font-size: 13px;">InvalidChoiceExceptions&nbsp;is handled by displaying the<br>current stage and asking user to select from the given list in current<br>stage<br>4)&nbsp;</span><span style="font-size: 13px;">ExceededRemainingChoicesExceptions&nbsp;is handled by displaying that message to user and then moving<br>on to next stage by adding value 1 to current enum value<br>5)&nbsp;</span><span style="font-size:<br>13px;">InvalidPaymentException&nbsp;is handled by displaying that message to user and then asking user to<br>enter the value in given currency format</span><br></li><br></ol><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Test Cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of test cases per the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/226503514-554b5ff2-c1e0-4b3f-ac37-924379d7f8a6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing three pytest fixtures <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/226503691-6182dfa7-a989-442a-8fee-e6bdd43eae11.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of other two fixtures<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/226505089-de07e5a4-e3f2-4bd9-9eeb-cf749a36422c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Test 1 and it&#39;s Output as shown in terminal<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/226505421-8b41ef31-1f4a-4578-a1d0-4b616e7348cd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Test 2 and it&#39;s Output as shown in terminal<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/226505688-09e0811e-97f5-49af-9aad-c6ced4d5564a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Test 3 and it&#39;s Output as shown in terminal<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/226505793-75c307f3-1ec9-40b2-b447-607c499567b0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Test 4 and it&#39;s Output as shown in terminal<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/226505895-bd3d8ad5-94c4-429e-b80d-052fec335343.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Test 5 and it&#39;s Output as shown in terminal<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/226510093-316edd45-bbaf-49f3-bf5b-707abc63406c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Test 6 and it&#39;s Output as shown in terminal<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/226506378-787334ed-5f55-4794-b411-5043afd9bcbf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Test 7 and it&#39;s Output as shown in terminal<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/226506566-3da1da68-f0c7-47dc-9e62-3e7de24c2f68.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Test 8 and it&#39;s Output as shown in terminal<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each test case logic</td></tr>
<tr><td> <em>Response:</em> <p>1)First test cases uses second_order fixture which is cascaded with two other fixtures.<br>The test is designed to simulate an invalid stage selection, where we attempt<br>to choose patty and toppings without selecting a bun. As expected, this triggers<br>the InvalidStageException. We then proceed to select a bun, which is allowed without<br>any issue.<div><br></div><div>2)Second test case uses third_order fixture to populate data which is chained<br>with three other fixtures. The purpose of the test is to verify the<br>behavior when certain patties are out of stock. We first attempt to select<br>three servings of turkey patty, but the stock for that item is limited<br>to two servings, so the expected outcome is an OutOfStockException being raised. Then,<br>we attempt to select a beef patty, which is currently in stock, and<br>it is allowed without any issues.</div><div><br></div><div>3)Third test case uses third_order fixture to populate<br>data which is chained with three other fixtures. The purpose of the test<br>is to verify the behavior when certain toppings are out of stock. We<br>first attempt to select three servings of cheese toppings, but the stock for<br>that item is limited to two servings, so the expected outcome is an<br>OutOfStockException being raised. Then, we attempt to select a tomato topping, which is<br>currently in stock, and it is allowed without any issues.<br><br>4)Fourth test case uses<br>machine fixture which just a burgermachine instance. In this test case we try<br>to check if combination of patties are allowed upto 3 patties and then<br>when we try to select fourth patty it raises an&nbsp;ExceededRemainingChoicesException as expected<br><br>5)Fifth test<br>case uses machine fixture which just a burgermachine instance. In this test case<br>we try to check if combination of toppings are allowed upto 3 toppings<br>and then when we try to select fourth patty it raises an&nbsp;ExceededRemainingChoicesException as<br>expected<br><br>6)sixth test case which contains different orders with different combinations of usable and<br>calculate cost is checked to see if the right value is calculated for<br>the orders<br><br>7)Seventh test case uses permute order fixture which is chained with three<br>other test cases. So three orders haven been completed because of cascading of<br>fixtures and assert statement is used in the test case to check the<br>value of total sales<br><br>8) eight test uses permute order fixture which is chained<br>with three other test cases. So three orders haven been completed because of<br>cascading of fixtures and another order is completed in the fixture. Assert statement<br>is used to check the burger count by checking the attribute total burgers.<br><br></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request for the assignment</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/ravella10/IS601-006/pull/18">https://github.com/ravella10/IS601-006/pull/18</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain any issues/difficulties or something you learned while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <ol><br><li>Had difficulties with cascading fixtures<br>2) because of the patties and toppings list<br>being class variable even when all the test cases ran still the quantities<br>are not resetting. Changing them to instance variables actually allowed me to run<br>all the test cases because quantities are reset to 0 in machine fixture<br><br><br></li><br></ol><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of successful output</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/226511923-5b60e78e-7fc6-4ecf-8bd3-7bb8100caf2a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1 Screenshot of successful program execution<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/226512209-045088e2-e3a1-440f-9c9c-93780cc6d215.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#2 Screenshot of successful program execution<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-2-burgers/grade/pr457" target="_blank">Grading</a></td></tr></table>