<table><tr><td> <em>Assignment: </em> IS601 Milestone 3 API Project</td></tr>
<tr><td> <em>Student: </em> Praneeth Ravella (pr457)</td></tr>
<tr><td> <em>Generated: </em> 5/8/2023 9:40:02 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone-3-api-project/grade/pr457" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone3 branch</li><li>Create a new markdown file called milestone3.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone3.md</li><li>Add/commit/push the changes to Milestone3</li><li>PR Milestone3 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 4</li><li>Submit the direct link to this new milestone3.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on GitHub and everywhere else. Images are only accepted from dev or prod, not localhost. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> API Data Association </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> How will this data relate to the User</td></tr>
<tr><td> <em>Response:</em> <p>#1) User can add entities to his/her watchlist.<div>These entities are Football teams, Football<br>leagues</div><div><br></div><div>#2)Once the user adds teams or leagues to his/her watchlist. Information such as<br>standings, statistics, live results and fixtures of these entities can be viewed by<br>user</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Data changes</td></tr>
<tr><td> <em>Response:</em> <ol><br><li>Teams and Leagues are associated to user watchlist through league id and<br>team id which won&#39;t change (according to API documentation) and if the user<br>were to update his/her watchlist the association&nbsp;<div>is updated in the database.</div><div><br></div><div>2) This is<br>a many to many relation as user can be associated with multiple teams<br>and leagues</div><br></li><br></ol><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Show how/where the user can associate the data with themselves</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/236823874-7bba6d64-3d25-4f17-b858-3dc1917ba4c9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the page where user can add league entity to watchlist with<br>help of dropdown data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/236824223-17647edc-3794-4a78-8b81-76aca20c0413.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the page where user can add team entity to watchlist with<br>help of dropdown data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/236824819-8b690bf5-6bd1-4e06-a354-5fa229ef8fad.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the code logic for associating the data to the user<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/236837627-4c6beb86-6988-43c2-9547-f6af4ad6ef1c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the code logic for associating the data to the user<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/236825567-549f2ab6-9926-4468-b9ff-f97cc327de78.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the code logic for pulling the entity data from endpoints and<br>storing in database<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/236838604-3460ad56-de9f-46c3-bd04-5cdaf62f00e1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of DB table for user and league entity association<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/236838770-9d1e81ac-253c-49ce-9b22-dba7abed03f7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of DB table for user and team entity association<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> List Associated Entities to the logged in user </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show the page where a user can list related/associated entities</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/236821370-41c4bec0-c032-48c7-aa5d-fbf7c7d365fa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing total count of team and league entities associated with current user<br>as a flash message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/236821475-f8fdbeae-ce65-49bf-b13a-786a44769cf7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing non-standard filter (country name)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/236821843-21cf40c9-bf98-476c-902b-7b16d7f1123c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing non-standard filter (team name)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/236822021-0fbea61a-18f5-4a9d-9e08-8f729a43ae13.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of output when limit applied to 2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/236822348-22768e7e-346d-4c55-94df-983cd44305d3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing that association of an entity is removed from user. Message is<br>visible on top<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/236823071-f7677af5-6792-40cf-a896-df6fa31ea6f0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of associations before clearing all the leagues<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/236823261-3bda8183-d73d-44d1-bc07-6ce1ece3e0b6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing output after all associations are cleared at once. showing success message<br>for deleting all and warning for not finding any leagues (as we just<br>deleted them)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/ravella10/IS601-006/pull/52">https://github.com/ravella10/IS601-006/pull/52</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> List entities associated with users </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show a page that lists entities that are associated with at least 1 user</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/236812793-4cb1d2c9-6dff-43b3-87c6-bace5490b6bb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing entities associated with at least 1 user and column showing the<br>number of users associated with each entity<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/236813418-d06146e8-5564-4576-9bb4-30cbb1346dbd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing filter on non-standard field which filters out based on the entity<br>type. Above screenshot filters and shows only team entities associated with at least<br>1 user<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/236813963-3d449735-c32b-469b-92b4-aafe349e16f0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing filter on non-standard field which filters out based on the entity<br>type. Above screenshot filters and shows only League entities associated with at least<br>1 user<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/236816183-6a0d2389-1306-43da-8390-ef3114c062ff.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing limit 1 applied on each entity separately (1 league record and<br>1 team recrod)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/236816741-069abbc9-da5d-4970-be6c-c46f43b55b85.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing limit 1 applied to only team by applying entity filter on<br>team<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/236817553-0cedcc44-a25b-4b3a-b175-f0cc7c94c013.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing sorting applied on count in desc order<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/236817846-99200e76-93bd-4191-a010-04a3e09fb923.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing filter applied on count &lt; 3<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/236834340-65bffa4c-86af-4824-aa7c-ce68ea003a94.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing entities data not associated with any users<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/ravella10/IS601-006/pull/53">https://github.com/ravella10/IS601-006/pull/53</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Admin Association Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Admin page to search for users and entities</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/236818686-dd0b5a1a-59ad-4a40-8f27-c74216a2113b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of page where admin can associate an entity to user. Email search<br>can be used to filter out users<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/236819186-bb3dff6e-80b8-4a64-8843-efcc7d20471a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of page where admin can add an entity to a user (In<br>this case username is erenyeager)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/236819400-20a63b0c-78d3-48a3-b964-95eea4ccbbc2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing added association wolves entity to eren yeager<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/236819593-a407ff24-80f8-4710-91cd-ca85e4d65b4a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing wolves association record( which was previously add) deleted using remove<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/ravella10/IS601-006/pull/53">https://github.com/ravella10/IS601-006/pull/53</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Project Related Screens not yet shown </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of other pages not yet shown</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/236820218-f24efc78-8907-410d-b75b-c6f48f0dacd2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing landing page which contains recent and live fixtures (no specific team<br>or league) with results. Common for all users<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/236827084-31d8c54f-8e21-4a32-9867-6fdbb18f35e1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing League entity in current user watchlist. Clicking on fixtures and live<br>results will lead to page shown next<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/236826454-2da0e9f7-a65c-4328-9f0d-86dcf47deb12.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing fixtures, live, finished and scheduled data for a specific league entity(la<br>liga in this case) along with date selector select specific date<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/236827564-89582369-be32-4866-9cf6-43f76dd6e0ba.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing Team entities in current user watchlist. Clicking on view stats will<br>lead to the page shown next<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123982470/236828128-677f8b79-e35d-4bfb-89da-9785d3cdc542.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing team stats of a team entity (manchester united in this case)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain each screen shown above</td></tr>
<tr><td> <em>Response:</em> <p>Landing page pulls data from the API with help of widget provided by<br>FootballAPI. This data shows the recent fixtures of all the leagues.<div><br></div><div>#1) Screenshot showing&nbsp;fixtures,<br>live, finished and scheduled data for a specific league entity is also obtained<br>from API with help of Games widget, data displayed can be changed using<br>tags of widgets.<br>#2) Initially league entity is added to watchlist by the user.<br>clicking on the fixtures and live results of a specific league will send<br>league_id as parameter to fetch the data<br><br>#1)Screenshot showing game stats of a team<br>which is obtained from&nbsp;<b><a href="https://v3.football.api-sports.io/teams/statistics">https://v3.football.api-sports.io/teams/statistics</a> </b>endpoint. league_id and team_id along with season are sent<br>as query<br>&nbsp; &nbsp; &nbsp; &nbsp;parameters to endpoint to fetch the data<br>#2) Initially Team<br>entity is added to watchlist by the user. clicking on the team stats<br>of a specific team will lead to stats page where data is fetched<br>by sending league_id, team_id and year</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/ravella10/IS601-006/pull/54">https://github.com/ravella10/IS601-006/pull/54</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>Learned&nbsp;data handling and manipulation, such as parsing JSON data and storing it in<br>a database<div>had to use Jinja templates extensively, referred to&nbsp;<a href="https://realpython.com/primer-on-jinja-templating/">https://realpython.com/primer-on-jinja-templating/</a> and jinja official documentation<br>for help</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone-3-api-project/grade/pr457" target="_blank">Grading</a></td></tr></table>