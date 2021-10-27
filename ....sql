-- 查询部门编号为30的员工
SELECT ename,deptno
FROM t_employees 
WHERE deptno = "30"

-- 查询所以经理
SELECT empno,ename,deptno
FROM t_employees
WHERE job = "经理"

-- 奖金高于工资的员工
SELECT *
FROM t_employees 
WHERE comm > sal

-- 奖金高于工资60%的员工
SELECT *
FROM t_employees 
WHERE comm > (sal*0.6)


-- 部门编号为10中所有经理，和部门编号为20中所有分析员的详细资料
 SELECT * 
 FROM t_employees
 WHERE (deptno=10 AND job="经理") or(deptno=20 AND job="分析员")

-- 部门编号为10中所有经理，部门编号为20中所有分析员，还有即不是经理又不是武装上将但其工资大或等于3000的所有员工详细资料。
SELECT * 
FROM t_employees 
WHERE (deptno=10 AND job="经理") OR (deptno=20 AND job="分析员") OR (sal>=3000 AND job!="经理" AND job!="武装上将")

-- 无奖金或奖金低于1000的员工
SELECT * 
FROM t_employees 
WHERE comm<1000 OR comm IS NULL

-- 查询名字由三个字组成的员工
SELECT * 
FROM t_employees 
WHERE ename LIKE "___"

-- 查询2000年以及以后入职的员工
SELECT * 
FROM t_employees 
WHERE hiredate LIKE"2___-%"

-- 查询所有员工详细信息，用编号升序排序
SELECT * 
FROM t_employees 
ORDER BY empno ASC

-- 查询所有员工详细信息，用工资降序排序，如果工资相同使用入职日期升序排序
 SELECT *
 FROM t_employees 
 ORDER BY sal DESC,hiredate ASC

-- 查询每个部门的平均工资
SELECT b.deptno,AVG(a.sal) 
FROM t_employees  a,t_dept  b
WHERE a.deptno = b.deptno
GROUP BY a.deptno 

-- 查询每个部门的雇员数量
SELECT deptno,COUNT(1)
FROM t_employees 
GROUP BY deptno

-- 查询每种工作的最高工资、最低工资、人数
SELECT job,MAX(sal),MIN(sal),COUNT(1)
FROM t_employees
GROUP BY job