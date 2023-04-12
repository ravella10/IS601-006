<table><tr><td> <em>Assignment: </em> IS601 Mini Project 3  Business Management</td></tr>
<tr><td> <em>Student: </em> Praneeth Ravella (pr457)</td></tr>
<tr><td> <em>Generated: </em> 4/11/2023 11:37:29 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-3-business-management/grade/pr457" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <div>Initial Preperation:</div><div><ol><li>Create two new dynos/VMs in Heroku:</li><ol><li>is601-ucid-mp3-dev</li><li>is601-ucid-mp3-prod</li></ol><li>Configure the heroku config vars and github secrets similar to how dev/prod were setup</li><li>Create two new secrets for github and set the values per the machine names in step 1</li><ol><li>HEROKU_APP_MP3_DEV</li><li>HEROKU_APP_MP3_PROD</li></ol><li>Duplicate your dev/prod yml files and have it listen to the mp3-dev and mp3-prod branches respectively</li><ol><li>Make sure you refer to the proper app secrets from step 3</li><li>You can merge these into regular dev/prod later but you'll want your final project to deploy over it (overwrite) on the normal dev/prod dynos/VM</li></ol><li>You can add this HW branch to the dev yml to test your deployments prior to the pull request to dev from step 4</li></ol></div><div><br></div><div><br></div><ol><li>checkout dev and pull any latest changes</li><li>Create a branch called mp3-prod and immediately push it</li><li>Create a branch called mp3-dev and immediately push it</li><li>Create a branch called MiniProject-3</li><li>Add all the baseline files first under a folder called BusinessManagement (included below)</li><li>Don't forget to copy your .env file from flask_sample into BusinessManagement</li><li>source the venv and pip install the requirements.txt</li><li>Run the BusinessManagement/sql/init_db.py script</li><li><b>Immediate add/commit/push to github</b></li><li>Open a pull request to mp3-dev and keep it open until you're done adding the submission file</li><li>Make your code changes per the following requirements</li><ol><li>Important: run the test files indiviudally as you're working/testing to save on query quota usage</li><li>&nbsp;pytest BusinessManagement/test/name_of_test.py -rA</li></ol><li>Add/commit periodically (recommended after you implement a TODO item or checlist item and add a related commit message for clarity)<br></li><ol><li>Do not delete any provided comments</li></ol><li>Anywhere relevant add your ucid and the date you added the code (best to do this as you go)</li><li>You'll be capturing website screenshots from dev and code snippet screenshots (ensure you upload these properly as pull request comments to the pull request from step 10</li><ol><li>Note: You don't need separate screenshots for each checklist item, when possible it's recommended to try to capture multiple items together and reuse the image</li><li>Ensure all screenshots are properly captioned in the deliverable section so it's clear what part you're trying to show</li></ol><li>Once done, copy the markdown or download the md file and save it under the BusinessManagement folder</li><li>Do a final add/commit/push</li><li>Verify everything looks ok in the pull request</li><li>Merge the pull request</li><li>Make a new pull request from mp3-dev to mp3-prod and merge it</li><ol><li>If you want to keep original dev/prod up to date you can merge the changes into those, but they will cause a deploy to occur for each so be mindful</li></ol><li>Navigate to the submission file under the BusinessManagement folder from mp3-prod</li><li>Copy the github url to the exact file and submit it to Canvas</li></ol><div>You'll be implementing a basic Business Management site.</div><div>There will be some provided files fully working as-is and some skeleton files you'll need to fill in.</div><div>The files you need to fill in will have TODO items or comments mentioning what's expected.</div><div>Some files will have "DO NOT EDIT" mentioned, please don't edit these. If there's a doubt about any of them ask.</div><div>There are provided test case files too that all must be passing for full credit. Do not edit these test case files.</div><div>If a test case isn't possible to complete, capture the failed test case locally via `pytest BusinessManagement -rA` first, then you can rename the function to `off_original_name`.</div><div>The site will handle CRUD operations for Companies and Employees as well as allowing import of Company/Employee data via a csv file.</div><div>Note: db.py has been updated to use pymysql instead of mysql-connector-python to aid in easier queries.</div><div><br></div><div>Baseline files:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F23-MiniProject-3">https://github.com/MattToegel/IS601/tree/F23-MiniProject-3</a>&nbsp;</div><div>May want to download branch as a zip, then copy/paste the files into your repo (if/when you do, please immediately do a git add/commit to record the baseline items)</div><div><br></div><div>Provided files you don't need to edit:</div><div><ul><li>000_create_table_companies.sql</li><li>001_create_table_employees.sql</li><li>db.py</li><li>init_db.py</li><li>flash.html</li><li>company_dropdown.html</li><li>country_state_selector.html</li><li>upload.html</li><li>sort_filter.html</li><li>all test files</li><li>geography.py</li><li>__init__.py (remains empty)</li><li>Dockerfile</li><li>main.py</li><li>index.py</li></ul><div>All other files likely have requirements to fill in.</div></div><div><br></div></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Identity Edits and Setup </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the index page being displayed (from dev)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231324105-f4e054ed-fc3b-49c3-bacd-3d327e053e57.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshots of points 1,2 and 3<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231324376-84e10592-5657-4e14-957f-0b8182d79f7d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshots for points 4 to 8, UCID at the top (DIAR-ucid<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot from the DB extension of vs code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231324712-42d69ee9-d63c-416a-9d04-52e38f05460a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing IS601_MP3_Companies table with UCID/DB name visible<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231324853-a69adc7b-6b2c-4df1-9fe8-e6710752ea71.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing IS601_MP3_Employees table with UCID/DB name visible<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Upload / Import CSV File (provided data.csv) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of /import route (code)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231332013-f182e27e-3873-4ef6-a90e-db00c8bc9979.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot checking if the file is a .csv file otherwise reject with a<br>flash<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231331316-b218305a-5b32-469d-91a0-4fa2e44ae01e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing extracting company and employee data appending it to list, displaying no<br>of records loaded or no records loaded<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231331561-cf5d3407-dc21-4602-a78b-5cf5077065a6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing number of employees loaded and flash message if no employees are<br>loaded<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of the website when uploading the data.csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231325001-d9431ca4-ae2a-4be0-9ba1-6c68babe98cb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the error message when the form was submitted without a file<br>attached<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231325152-2ab8b43f-7b1a-4b97-9609-bf077f775743.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the error message when the file is not a .csv file<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231326311-961b1eb3-a8a4-414f-898c-06a49f88382c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing proper success message and count message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data (basic summary/view)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231325960-46258198-f174-48fc-9e77-bed0c8c24086.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of company table without data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231326075-8ba5a2a9-8168-4152-8e36-a2756a471dbf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of employee table without data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231326628-c93b4578-6d05-4d91-9084-1dfcf54aceeb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of company table after inserting data from csv as show in above<br>sub-task screenshot<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231326692-7a34b1ba-e561-4e56-b005-a358990935fe.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of employee table after inserting data from csv as show in above<br>sub-task screenshot<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Add Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231332760-d8e9cf39-1fd1-410b-b9bb-98a0a6e5fac1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing logic for retrieving first_name, last_name, company (id), email. requiring first_name, last_name,<br>company<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231333016-52e93e37-5e7e-4c90-9855-fb5a5b66e345.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing logic for email is required and format is verified<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231333300-ae475182-c24d-4f36-b5fb-019923ea95c7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing logic Insert query with data and user-friendly message, print() of exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231297180-3d266c0a-2a70-4d94-8228-580dcc69d413.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing valid data filled prior to submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231297844-8866caf7-cba8-46df-92bc-61bac3491524.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of success message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231333760-cc41b7f0-3239-470d-8129-5ef9d434811f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of first_name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231333878-fdddc12e-a1f1-46a2-84ee-196872c16f51.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of last_name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231334002-d7da2ae6-150c-44da-b184-260a8bcaabb0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of email error message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new employee DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231301417-72479ed5-5fdd-4ee1-9cdd-cbc4092ed3b5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the valid employee (First name - Erwin, Last name - Smith)<br>data shown previously. <br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> List/search Employees </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231334438-b0b35a1a-eba5-4e06-843b-b0e9e222bc79.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the select query and logic for checking request args<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231334592-6b4b7310-1737-492b-9028-5c9864273ca7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing points #3 to #7. where we check if attributes are null<br>and append queries<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231334936-a9c396a0-9428-4e8d-9ec9-630f042929b5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing append limit with exception handling and checking limit values<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231302784-168cde2f-1b4c-461d-8705-3d0088dd1fcb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing results with first_name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231303045-8218c0e3-6879-450d-9b29-d0666c0bc5f8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing results with last_name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231303368-6856e4f1-2c5d-4358-8b60-df525d59cdbf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing results with email filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231327044-d56a46cd-27a8-4cbe-b90b-2620aac4fd62.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing results with company filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231327151-2c9268dc-ebf4-4bd4-8c58-848cfccf155b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing results with asc filter applied on column first_name<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231327341-e10dc35f-ff6a-4bae-bf4e-bb5fb5ec6c5e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing results with desc filter applied on column<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231335306-4cf47b32-cc36-4584-a830-1c7cfc6ebb0b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing retrieving data and checking if first_name and last_name are present<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231335559-49a1c4f8-7962-4b42-9467-5a5d3a7d2999.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the update query and checking for email<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231336058-8f41590f-aa80-4b8d-a2be-7b113523cd6f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing select query and exception messages<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231336319-ed7b52d8-e25b-40a7-89ca-a8d3d74f84db.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing data before edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231336459-6b427b09-6790-4fd9-b186-2ccd6c4f4ca9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing Successful edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231336536-6362dac6-b228-441d-a49b-9858993634a3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing after Edit<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of employee data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231336715-ee299fd7-b209-4159-81c8-5356bfb329d8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Data before edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231336871-f75eee2b-31d1-4dca-860f-8327d2915e2a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Data after edit<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231337152-2d2fdae9-e2f1-4034-be05-0dc66649980e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing logic for retrieving form data and checking for name,address,city<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231337322-a31d82a8-e362-446a-98f7-0fe625c0d480.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing logic for checking state and country, and also checking to see<br>if they are valid and present pycountry<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231337621-0dba6800-89b9-4a51-92cc-87999b6b4e76.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing logic for checking zipcode, website and insert query along the flash<br>message for exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231316036-5e810c98-1a49-4829-ba1a-6d4216603763.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of valid data prior to submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231316146-12a001a4-1494-4abb-9182-2ca66e5f1d23.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of success message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231341055-9922409d-b57d-476d-afa6-3032d3dfb739.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231341742-0d671c9d-df61-4ee0-809a-ba2930b132d0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of address error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231341266-d22051d3-f478-42d0-8dd9-dabc38b3056b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of city error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231341385-8cb50d0a-4f9b-4ff3-ada4-ee0a3e706e20.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of state error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231341573-30266f2e-9079-4bcd-a551-264b5c98a400.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of zip error message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new company DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231318258-c3e255a2-c4e2-4760-86a9-cb6d6371c9fb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot including the valid company data shown previously<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> List/Search Comapny </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231338093-2dfbcac0-4897-4eaf-a48c-33cddb031f19.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing select query and retrieving data, appending like filter to query<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231338325-2ff4abbd-1ece-4831-901c-50644029adcd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing points 4 to 8<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231338508-73c2c1d7-6b40-4e59-b235-22a7dca12b0f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing user friendly message flashed and a print() of the exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231318508-f5846be0-c79d-4d96-bd4d-595f6cf7c967.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing results with name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231318731-08f264f0-4d53-4b49-b6ae-10068276ebc4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing results with country filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231318843-a253afb7-4e80-4d9e-b768-335347f0b0c9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing results with state filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231319054-ff4d1ad0-2c45-462b-aa2c-dbee568beeda.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing one asc filter applied (Name is chosen as column)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231319166-2e6ef79b-8f67-4435-b106-36e816a88b7d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing one desc filter applied (Name is chosen as column)<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Edit Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231339426-a0bc6e87-c1d0-4cd5-8ab7-fad2294c7d5a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing retrieving data and checking name,id<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231339578-cb3f7c5b-5586-43dd-ae19-e26f9eb071e1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing checking for state,city and country. also checking if sate is present<br>in pycountries<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231339779-ef760a27-26aa-479e-92b7-ab1f4c45b24c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing checking for country, zipcode and if country is present in pycountires<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231339940-07d281f8-c201-404c-a973-39c6fcc3cd77.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing select query and update query along flash messages for exceptions<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231340178-a89faff1-48b1-4170-b48e-860f16886631.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Data before an edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231340392-dc3f06d5-bc07-41d1-9e67-8c03679e00ce.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit Successful message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231340463-5c4fa82d-86f9-4eb9-b412-0305a17bf8b2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edited name from Chanay, Jeffrey A Esq to Chanay, Jeff A Esq<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of company  data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231340265-cda362f7-1922-4579-9082-4dfcea7d5654.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Data before edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231340641-1068285e-ab32-430f-807c-7850204357f0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Data after edit, Edited name from Chanay, Jeffrey A Esq to Chanay, Jeff<br>A Esq<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Delete Employee and Delete Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /delete route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231321815-2d2088c1-04e8-4f5b-91f7-dae607561f7a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of delete() with all the points in checklist implemented<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after website screenshot of deleting an employee (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231319589-54d23326-8fa3-437e-8802-f5e3ee68a668.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of data before deleting<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231319717-49c78450-f89e-4324-bf4b-dd3e6395cc29.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot after deleting the data and also Success message flashed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of code for /delete route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231322163-4bb1706a-d9d3-4b9f-8f25-d60cc1f117e2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of delete() with all the points in checklist implemented<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after website screenshot of deleting a company (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231338719-4afdd944-173a-4cd1-aecd-28004aa74b4a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before deleting a company<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231339005-7638ba4a-ff6c-42cc-b246-26d0d206f8c2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing Success Message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231339145-b964b0c1-5053-4281-9c46-bdbe75c7d14f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After deleting the company<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Test Cases and Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot Test case Results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231322613-a89a2828-d4c7-41b0-b4e7-31a3c3c94bd9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of test_add_company.py<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231322760-d8985e7c-8c88-4d88-9db5-296db3a6de57.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of test_add_employee.py<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231323045-00b90e68-9c82-41cf-aa49-68354d9cba78.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of test_edit_company.py<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231323187-56cf22ab-4fb8-4cf8-a6fa-fd92a24a7fe7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of test_edit_employee.py<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231323336-34b23fb6-61c8-4bdf-83bf-dbc745cbef59.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of test_search_company.py<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231323460-8bc5c429-2267-4c9d-a807-8c121e0c41b0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of test_search_employee.py<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/231323579-3f369b39-5e78-4579-aa1d-e3cbc803fd3e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of test_upload_csv.py<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Issues / Learnings / Interesting things to note</td></tr>
<tr><td> <em>Response:</em> <div>I have learned how to handle GET and POST calls to perform actions</div><div>like<br>add, edit, sort, and delete. Learned how to use wtforms and pass</div><div>arguments to<br>it. Learned to write SQL queries in a pythonic way. Learned</div><div>to handle a<br>data(CSV) file and parse it. Learned to handle exceptions and</div><div>flash massages.</div><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-3-business-management/grade/pr457" target="_blank">Grading</a></td></tr></table>