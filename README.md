Markdown
# Corporate Structure Analytics Engine 📊🏢

## Overview
This project contains the database schema and analytical queries for a manufacturing company. It is designed to track employee allocation, department hierarchies, and project outputs to compare the operational efficiency of traditional functional structures against dynamic cross-functional teams.

## Features
*   **Relational Schema Design:** Normalized SQL tables for Departments, Employees, and Performance Metrics.
*   **Organizational Modeling:** Maps both rigid departments (e.g., Engineering) and flexible project groups.
*   **Performance Analytics:** Utilizes complex `JOIN` operations and aggregation functions to measure the average project output based on team structure type.

## Technologies Used
*   SQL (Standard DDL and DML)
*   Compatible with PostgreSQL, MySQL, or SQLite

## Setup Instructions
1. Initialize your preferred SQL database environment.
2. Execute `schema.sql` to build the tables and insert the sample organizational data.
3. Run the provided analytical queries to view team performance comparisons.
