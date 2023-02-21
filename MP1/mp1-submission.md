<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 1 - Tracker App</td></tr>
<tr><td> <em>Student: </em> Praneeth Ravella (pr457)</td></tr>
<tr><td> <em>Generated: </em> 2/20/2023 11:20:22 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-1-tracker-app/grade/pr457" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout dev branch and pull any pending changes&nbsp;</li><ol><li>&nbsp;git checkout dev</li><li>&nbsp;git pull origin dev</li></ol><li>Create a new branch for this assignment (see Desired Branch Name)</li><ol><li>git checkout -b MP1-Tracker</li></ol><li>Create a new folder called MP1 in your local repository</li><li>Create a new file called tracker.py</li><li>Copy/paste the content from this template:&nbsp;&nbsp;<a href="https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da">https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da</a></li><li>Add/commit/push the template file</li><ol><li>git add --all</li><li>git commit -m "adding template"</li><li>git push origin MP1-Tracker</li></ol><li>Create a pull request from MP1-Tracker to dev (keep it open, do not close it until you're done)</li><li>Solve the various todo items (also noted below in the deliverables) and fill in the evidence</li><ol><li>Periodically add/commit; recommended after each solved item or every few items</li></ol><li>Save and copy/download the markdown</li><li>Create a new file mp1-submission.md in the MP1 folder</li><li>Add the markdown content</li><li>add/commit/push all the pending files for this assignment (tracker.py and mp1-submission.md)</li><li>If everything looks good on the pull request complete the merge</li><li>Create a new pull request from dev to prod and merge it to update prod (not used yet but you want to keep this up to date)</li><li>checkout dev locally and pull the changes to be up to date</li><li>Navigate to the prod branch on github and find the mp1-submission.md file and get the link to the file to submit to canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Add Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited add_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/220240352-d8c9084d-a86e-4271-aa71-7ee0b6b708ba.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> screenshot of the edited add_task() function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of add_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/220240904-18185f3b-ee74-4edd-af56-6e5161f208bc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of added task message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/220241247-461cd739-6352-47c5-b42e-1339e242a20e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of message saying task not added due to missing name<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/220241453-31e30444-15a4-40c1-b969-9200473664fa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of message saying task not added due to wrong due date format<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/220241597-0b6fe2ec-0f0e-4506-8df4-cea710401971.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of message saying task not added due to missing description<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for add_task()</td></tr>
<tr><td> <em>Response:</em> <p>Message dictionary which contains different messages for different outputs<div>If conditions are used to<br>check the missing data and if any missing data is found then message_key<br>variable is updated with respective value</div><div>This message_key is passed to message dictionary which<br>would print out the right message for failing to add the task</div><div>If there<br>is no missing data then the task is added to tasks list and<br>message is printed saying task is added successfully. datetime.now() is used to assign<br>the value to &#39;lastActivity&#39;</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Process Update Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited process_update() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/220239200-48822ab9-0e36-4e6f-a712-39c5934a1cbc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the edited process_update() function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain the solutions to the checklist items for process_update()</td></tr>
<tr><td> <em>Response:</em> <p>checks if the index is out of bounds, prints an error message if<br>it is or else the task is retrieved by index<div>The existing value of<br>each property are included in input prompt f-string by putting the variables(name, description<br>etc) in curly braces({})</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Update Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited update_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/220242474-c1f659c9-973c-4afb-930c-7a179087be8e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the edited update_task() function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of update_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/220243213-5d307ed9-4d99-4bc3-b2fc-0e09a08e402a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing a relevant message about the task being updated<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/220242992-c6c623fd-0db8-4d65-8021-943cff9187f5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing a relevant message about no changes to save or no changes<br>provided<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for update_task()</td></tr>
<tr><td> <em>Response:</em> <p>checks if the index is out of bounds, prints an error message if<br>it is or else the task is retrieved by index<div>Once the task is<br>retrieved, if conditions are used to check what data is provided. If the<br>data is not missing then the respective value in the task are updated<br>and rest are left the same.</div><div>Using the index the new task updated in<br>tasks list. flag is used inorder to check if any of the data<br>is updated. It is false if nothing is changed and prints the respective<br>message or else is true if updated and prints the respective message. if<br>it the any of the information is updated then the lastActivity is updated<br>with current datetime using datetime.now()</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Mark Task Done/Complete Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited mark_done() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/220216230-007f533f-0bb7-4fc9-8910-50f8227fc4cc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of of the edited mark_done() function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of mark_done()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/220217767-c236d194-f755-4d82-a4e0-1d3fa972717e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the output showing task being marked done/complete<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/220217921-15864384-7e83-40f7-ae39-3bae1df287c7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the output showing task already being done/complete<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for mark_done()</td></tr>
<tr><td> <em>Response:</em> <p>checks if the index is out of bounds, prints an error message if<br>it is or else the task is retrieved by index<div>If the retrieved task<br>is not yet completed then assign current datetime or else print task is<br>already completed<br><div><br></div></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> View Task Logic (and list) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited view_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/220220341-faecf7a0-e48c-4e34-8691-3123974e324e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the edited view_task() function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of view_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/220220763-58b38942-0ca0-44f1-a00d-66769f1984e2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the task info (given: check list, task name, task description, last<br>activity, due, and completed)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/220220847-67f803a7-b8ce-4ce7-81d0-6d6537c3936a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the related message about task not found or invalid task number<br>or similar<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot(s) of list_tasks() output showing a few examples</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/220221468-04bf34d1-e56f-4b57-9d94-7d30fea0c337.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> screenshot of list_tasks() output showing a few examples<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Delete Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited delete_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/220221645-8852d7e6-c658-48c4-b129-dd70ece89d4b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the edited delete_task() function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of delete_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/220222846-cea82d11-6b2b-47f8-a508-cb3c630cb68e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of related message about task being deleted/removed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/220222945-ad682fcd-1cb5-49f1-b558-0921a9c63678.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of related message about invalid task/number or similar<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for delete_task()</td></tr>
<tr><td> <em>Response:</em> <p>checks if the index is out of bounds, prints an error message if<br>it is or else the task is retrieved by index<div>deletes the task with<br>given index from tasks using del keyword<br></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Get Incomplete Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_incomplete_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/220231058-8cb8dcb6-b8e2-45f9-a888-648b7666e6e7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the edited get_incomplete_tasks() function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_incomplete_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/220229114-85fb140a-7a99-45c2-833a-1c9b9876211c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of at least 1 incomplete task<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/220245135-8ed9960a-f145-4a39-ab6f-ee813d05ceea.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of some message about no tasks<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_incomplete_tasks()</td></tr>
<tr><td> <em>Response:</em> <div>list comprehension to retrieve all the tasks that are not done yet by<br>checking if the value of 'done' key is false<br></div><div>if the _tasks list is<br>empty then prints no incomplete tasks or else prints the tasks in list<br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Get Over Due Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_overdue_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/220244416-2e1e28a0-751b-4186-8246-ff0804f40ee2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the edited get_overdue_tasks() function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_overdue_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/220244659-faca2e74-c33c-441e-b034-baa7a64f94e9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing at least 1 over due task<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/220244878-f3979b8a-f800-4514-9284-89e5ac4ff8fa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot Showing message about no tasks<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_overdue_tasks()</td></tr>
<tr><td> <em>Response:</em> <div>list comprehension to retrieve all the tasks past due date by using if<br>condition to compare the due datetime with current datetime and checks if the<br>task is completed or not.</div><div>if the _tasks list is empty then prints no<br>overdue tasks or else prints the tasks in list<br><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Get Time Remaining Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_time_remaining() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/220232205-baeb01f4-0bc5-42e2-b4b7-231294bf8adb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the edited get_time_remaining() function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_time_remaining()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/220232996-1a2ee156-ad94-487d-8276-dc95e6957371.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of how many days, hours, minutes, seconds until due<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/220233742-2c532577-4cd0-456c-8593-f946fbf821dc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of message showing due by days, hours, minutes, seconds<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_time_remaining()</td></tr>
<tr><td> <em>Response:</em> <p>Compares the current datetime with the task due datetime and finds the difference<br>between depending on which is greater and prints the message accordingly.&nbsp;<br>The time difference<br>is taken is seconds and then division and mod operations are performed(using divmod<br>method) to get the days, hours, minutes, and seconds<div>Mod operation is used to<br>get remainder time where division is used for conversion.</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of program output generated from filling in this deliverable (or close to it)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/220245421-fb050621-4096-41e3-894e-e02de630daff.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of adding task<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/220245539-e133ee7c-c694-4ccc-800c-6acb68de5ac3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of listing tasks<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/220245654-51c40a89-6a40-4a20-ba1e-91bedf5200a3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of updating and viewing the specific task <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/220245815-258a44d4-41d9-49ae-88bd-a17678861239.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of marking an task as done and then deleting the task<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) of the saved JSON file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/220236203-32ab8201-01bb-432e-9152-9f751fdb1ebf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the saved JSON file<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Discuss any issues and how they were overcome or learnings from this project</td></tr>
<tr><td> <em>Response:</em> <p>Faced some issue with converting the date difference into days, hours, minutes, seconds<br>format, had to look up on web to understand how it&#39;s done<br><br><br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add pull request for this assignment (project branch to dev)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/ravella10/IS601-006/pull/5">https://github.com/ravella10/IS601-006/pull/5</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-1-tracker-app/grade/pr457" target="_blank">Grading</a></td></tr></table>