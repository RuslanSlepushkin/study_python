select first_name, last_name, employees.department_id, department.department_name 
from employees 
join department on employees.department_id = department.department_id;

select first_name, last_name, department.department_name, locations.city, locations.state_province
from employees 
join department on employees.department_id = department.department_id
join locations on department.location_id  = locations.location_id;

select first_name, last_name, employees.department_id, department.department_name 
from employees 
join department on employees.department_id = department.department_id 
where employees.department_id in (80, 40);

select department.department_id, department.department_name 
from department
left join employees on department.department_id = employees.department_id;

select f_t.first_name as employee_first_name, s_t.first_name as manager_first_name
from employees f_t
join employees s_t on f_t.manager_id = s_t.employee_id; 

select jobs.job_title, first_name ||' '|| last_name as full_name, 
jobs.max_salary - employees.salary as difference_salary 
from employees
join jobs on employees.job_id = jobs.job_id;

select jobs.job_title, avg(employees.salary) as average_salary
from employees
join jobs on employees.job_id = jobs.job_id
group by jobs.job_title;

select first_name ||' '|| last_name as full_name, employees.salary 
from employees 
join department on employees.department_id = department.department_id
join locations on department.location_id  = locations.location_id
where city = 'London';

select department.department_name, count(department.department_id) as number_employees_department
from employees
join department on employees.department_id = department.department_id
group by department.department_name;