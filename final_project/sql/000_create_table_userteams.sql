CREATE TABLE
    IS601_UserTeams(
        user_id int not null,
        team_id int not null,
        PRIMARY KEY(user_id,team_id)
    )