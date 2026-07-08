-- 1. Create the schema
CREATE TABLE Departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50),
    structure_type VARCHAR(50) -- e.g., 'Functional', 'Cross-Functional'
);

CREATE TABLE Employees (
    emp_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES Departments(dept_id)
);

CREATE TABLE PerformanceMetrics (
    metric_id INT PRIMARY KEY,
    emp_id INT,
    quarter VARCHAR(10),
    projects_completed INT,
    FOREIGN KEY (emp_id) REFERENCES Employees(emp_id)
);

-- 2. Insert sample data (Widgets 'R Us example)
INSERT INTO Departments (dept_id, dept_name, structure_type) VALUES 
(1, 'Engineering', 'Functional'),
(2, 'Project Tiger', 'Cross-Functional');

-- 3. Complex Query: Compare output of functional vs cross-functional teams
SELECT 
    d.structure_type,
    SUM(p.projects_completed) AS total_projects,
    AVG(p.projects_completed) AS avg_per_employee
FROM 
    Departments d
JOIN 
    Employees e ON d.dept_id = e.dept_id
JOIN 
    PerformanceMetrics p ON e.emp_id = p.emp_id
GROUP BY 
    d.structure_type;