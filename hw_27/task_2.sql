select first_name as first_name, last_name as last_name from employees;

select distinct department_id from employees;

select * from employees order by first_name desc;

select first_name, last_name, salary, salary * 0.12 as PF from employees;

select max(salary) as maximum_salary, min(salary) as minimum_salary from employees;

select first_name, last_name, round(salary/12, 2) as monthly_salary from employees;