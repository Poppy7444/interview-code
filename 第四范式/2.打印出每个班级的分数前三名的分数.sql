/* 题目描述
SQL 编程
打印出每个班级的分数前三名的分数(假设所有学生中没有分数相同的情况, 也就是不考虑并列第一第二第三的场景)
表结构：
id varchar(20),-- 编号
class varchar(20),-- 班级
score int-- 分数
 */

-- 1
select * from  student s where (select count(*) from student where s.class=class and s.score<score) <3;
-- 2
select * from student t where exists(select count(*) from student ts  where ts.score>=t.score and ts.class=t.class group by ts.class having count(*)<=3)
order by class,score desc;