-- removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0.
-- cat 13-change_class.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
-- se changes:
-- cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

DELETE FROM second_table WHERE score <= 5;