<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Praneeth Ravella (pr457)</td></tr>
<tr><td> <em>Generated: </em> 4/17/2023 11:35:56 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone1-deliverable/grade/pr457" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone1 branch</li><li>Create a milestone1.md file in your Project folder</li><li>Git add/commit/push this empty file to Milestone1 (you'll need the link later)</li><li>Ensure your images display correctly in the sample markdown at the bottom</li><ol><li>NOTE: You may want to try to capture as much checklist evidence in your screenshots as possible, you do not need individual screenshots and are recommended to combine things when possible. Also, some screenshots may be reused if applicable.</li></ol><li>Save the submission items</li><li>Copy/paste the markdown from the "Copy markdown to clipboard link" or via the download button</li><li>Paste the code into the milestone1.md file or overwrite the file</li><li>Git add/commit/push the md file to Milestone1</li><li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li><li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku dev</li></ol></li><li>Make a pull request from dev to prod (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku prod</li></ol></li><li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/232647183-4ae71e1d-136f-402f-82d4-ec3281aedb57.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of username not available <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/232647488-d43bad9d-0047-4a4a-88bd-05ee238e1326.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of email not valid<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/232647678-5cb4c850-3579-4edc-a7d3-6e8ba00b7c78.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of invalid password validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/232647899-c183b55e-0231-4019-bb23-8baee8ce7114.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of passwords not matching<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/232648224-6720e8bf-26c4-47a7-bbec-a1d000cd5a9a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of email not available<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/232648656-da22a441-ede7-4a07-9386-0618cfda0cfd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of valid data filled in before the form is submitted<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/232648953-007ecaa8-d07c-4f0d-bff2-e614f558dd1f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of user data from Task 1<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/ravella10/IS601-006/pull/38">https://github.com/ravella10/IS601-006/pull/38</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p><font color="#1f2328" face="-apple-system, BlinkMacSystemFont, Segoe UI, Noto Sans, Helvetica, Arial, sans-serif, Apple Color<br>Emoji, Segoe UI Emoji"><span style="font-size: 16px;"><div style="">1) Form is handled with wtforms and<br>each field has its own validation. The</div><div style="">form can only be submitted successfully<br>once all the fields have met the</div><div style="">requirement.</div><div style=""><br></div><div style="">2)&nbsp;<span style="font-family: Roboto, -apple-system,<br>&quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; font-size: 14px;">Validation is done with the help wtforms<br>validators which work for both frontend</span></div></span></font><div>and backend. The following validators are used:&nbsp; DataRequired()<br>is used to mark the</div><div>field as required, EqualTo() is used to check if<br>the password and confirm-password</div><div>match and Email() is used to check for valid email<br>format. Username is</div><div>checked to match &quot;^[a-z0-9_-]{2,30}$&quot; this regex. Duplicate username and email values<br>are checked</div><div>during the inserting into the database. A flash message is populated for<br>a</div><div>duplicate entry exception.<br></div><div><br></div><div>3) Password is hashed with bcrypt and then saved into the<br>database.</div><div><br></div><div>4) All the form data is saved in the users table&nbsp; which is<br>created in the database along with the created and modified timestamp.</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/232649985-084fc944-f939-4720-88d8-ee1aca190135.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of mismatch validation <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/232650171-910815e8-d6c7-4db6-9e86-6842a9d20bfb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of validation based on non-existing user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/232650293-4c86e370-7ba2-42e5-a0ad-410ffdf2be52.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of a flash message and redirect to a landing page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/ravella10/IS601-006/pull/38">https://github.com/ravella10/IS601-006/pull/38</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div>1) Form is handled with wtforms and each field has its own validation.<br>The</div><div>form can only be submitted successfully once all the fields have met the</div><div>requirement.</div><div><br></div><div>2)<br>Validation is done with the help wtforms validators which work for both front-end</div><div>and<br>back-end.&nbsp; The "Email or Username" field accepts either email or username and</div><div>is validated<br>based on the input. If the username or email is not</div><div>present in the<br>database then a flash message saying "Invalid User" is displayed.</div><div><br></div><div>3) If the username&nbsp;<br>matches but not the password then a flash message saying</div><div>"Invalid Password" is displayed</div><div>Password<br>entered is matched with the hashed password which is</div><div>already present in the database.<br>A function bcrypt.check_password_hash() does this matching with the</div><div>help of salt value.</div><div><br></div><div>4) Both password<br>and email or username are matched with the</div><div>tuples in the database from users<br>table which holds the data while registering.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/232650656-98527431-2b96-415f-ad69-5d83d64a178d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of message showing something about being logged out<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/232660367-db51f066-0222-4a7d-af93-a7ff908bf713.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot should show something about not being logged in<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/ravella10/IS601-006/pull/39">https://github.com/ravella10/IS601-006/pull/39</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div>When the user logs in, the User object is stored in the session.</div><div>When<br>the page reloads, that User object in the session is used to</div><div>authenticate instead<br>of calling the database. Which helps in avoiding the overhead. If</div><div>the User object<br>is not present in the session then it loads from</div><div>the database.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/232660492-5ae4dc81-e542-43b2-9498-f161835e1c0d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of message showing error message because user can&#39;t access a login-protected page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/232660672-29a90bbb-4da9-4a78-9f71-b26dd140549b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of message should show something <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/232660839-ce6e4967-3c05-4e87-b263-06d0bd6304c6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of one valid record from the lessons (i.e., Admin)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/232661112-2da1ebc4-7810-4fad-8c31-ed9edf2166be.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of userroles table where the user with user_id 2 is admin user<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/232661245-e512a74d-03c7-406d-b3e8-b20f5bf87250.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of users table where the username ravella has the user_id 2 (admin<br>user)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/ravella10/IS601-006/pull/39">https://github.com/ravella10/IS601-006/pull/39</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <div>Login-protected pages are protected with the @login_required decorator provided by flask_login. This triggers</div><div>the<br>user_loader for each page request. The user will be loaded from the</div><div>session if<br>exists to avoid repeated database calls. If not present in the</div><div>session then it<br>loads from the database.</div><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <div>Role-protected pages are protected with the help of flask_principal. We define permission with</div><div>the<br>role needed for it. This permission can be imposed on the desired</div><div>pages by<br>prepending it with the permission decorators. The identity is loaded into</div><div>the session with<br>the user name and authentication type.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/232663038-5bee3dcd-082a-4958-91b0-c972961409c1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing styles navigation and register form. All the forms follow the same<br>theme<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/232663352-1145c93f-47d6-4ae5-b0a4-21da939dfac9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing styles navigation (after logging in) and tables.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/ravella10/IS601-006/pull/39">https://github.com/ravella10/IS601-006/pull/39</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <p>I have followed a dark theme for the nav and gray for the<br>forms. Chose a sample Navigation<div>from the bootstrap where the login, register, and log<br>out will be to</div><div>the right extreme separated from the main nav.&nbsp;</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/232661943-1469af98-100c-4984-93c9-ee4cae252e42.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of permission denied when trying to access without sufficient permissions<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/232662286-4eb06ee6-7f39-4b4e-ab57-755c8bfea0e5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of unauthorized access without logging in and trying to access this page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/232662782-f1bc3602-85e9-4de0-a664-2b53f8b259bd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of error showing page not found<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/ravella10/IS601-006/pull/39">https://github.com/ravella10/IS601-006/pull/39</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <div>For the HTTP server error messages like 401, 403, and 404 I have</div><div>created<br>separate pages with custom and user-friendly messages being displayed. If any of</div><div>those errors<br>occur it will be redirected to render its respective HTML page.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/232653177-cd88ba93-3f42-400f-84c0-7bb814c5e1db.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of email and username should prefill properly<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/ravella10/IS601-006/pull/38">https://github.com/ravella10/IS601-006/pull/38</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <div>When the profile page is loaded, the user id is fetched from the<br>current_user. With that user id email and username of that user is fetched<br>from the database and is populated to the respective fields.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/232653941-9312b570-4a78-4e33-b900-e328526e3ad3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of password mismatch message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/232654195-bdcdc4fa-28d2-4d03-b802-b8345ae09580.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of username validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/232654516-45e89ce4-36af-4a46-aaa3-142aabb5f5f3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of password validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/232654643-3c848a6b-7bc6-4921-bae0-e771ee0409d1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of email validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/232654945-046d2610-02d0-48ca-806a-8fab68c937a2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of email/username already in use<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/232655031-516b4323-cf42-496b-862d-bdd2bcdec488.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of email/username already in use<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/232655265-bd668469-bea5-4ee0-9f80-dbab005834e6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot before the record is edited<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/232655598-95e4cbf8-d966-4957-bdf3-7fb184d8253c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot after the record is edited<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/232655908-5eb77912-1379-41f8-b62f-d76875f79cc9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot after the record is edited (database screenshot)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/ravella10/IS601-006/pull/38">https://github.com/ravella10/IS601-006/pull/38</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em> <div>The username and email fields are updated for each update request. Before updating</div><div>the<br>username and email values, they checked if they match the required respective</div><div>format. If<br>yes then it checks if either of the values are already</div><div>being used by<br>other users in the database. If yes, then a flash</div><div>message is populated that<br>the respective value is not available for use. For</div><div>updating the password, we check<br>if the new password match with confirm password</div><div>and then check if the current<br>password is the same as the existing</div><div>password in the database. If these conditions<br>are satisfied then the password is</div><div>updated.&nbsp;</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>Faced some issues with styling of nav, login and registration pages with bootstrap,<br>gone through templates available online to implement styles.<div><div><div><div>For the HTTP server error messages<br>like 401, 403, and 404 I have</div><div>created separate pages with custom and user-friendly<br>messages being displayed</div></div></div></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Prod Application Link to Login Page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-pr457-prod.herokuapp.com/login">https://is601-pr457-prod.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone1-deliverable/grade/pr457" target="_blank">Grading</a></td></tr></table>