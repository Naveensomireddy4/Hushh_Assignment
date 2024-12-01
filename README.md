# Comprehensive Backend and ML Application Development

## Objective
This project is designed to evaluate proficiency in backend API development, database handling, prompt engineering, large language models (LLMs), and SQL-based data analysis. The project is divided into three main parts: CRUD operations API development, data processing pipeline, and metrics extraction and automation from SQL.

---

## Part 1: CRUD Operations API Development

### Database Schema

The following database schema is provided for the development of the API:

```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  user_id INT REFERENCES users(id),
  product_name VARCHAR(255) NOT NULL,
  quantity INT CHECK (quantity > 0),
  order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
# Requirements
## API Development: Build a FastAPI application to perform CRUD operations for both users and orders tables.
```
Endpoints for Users:
POST /users: Create a new user.
GET /users/{id}: Fetch user details by ID.
PUT /users/{id}: Update user information.
DELETE /users/{id}: Delete a user by ID.
Endpoints for Orders:
POST /orders: Create a new order.
GET /orders/{id}: Fetch order details by ID.
PUT /orders/{id}: Update order details.
DELETE /orders/{id}: Delete an order by ID.
```
# Concurrency: Use Uvicorn/Gunicorn with multiple workers to handle concurrent requests efficiently.

## Error Handling: Implement error handling for:

Invalid input (e.g., missing fields, incorrect data formats).
Database constraints (e.g., unique email violation, foreign key errors).
Resource not found (e.g., invalid user or order ID).
Security: Ensure the API uses SSL for secure communication.

Concurrency and Asynchronous Operations: Use async/await for database and I/O operations to maximize performance.

Testing: Write test cases for each API endpoint to ensure reliability and proper handling of edge cases.

# Part 2: Data Processing Pipeline with APIs
## Objective
## Integrate OpenAI or Gemini API to process text data and build a custom data processing pipeline.

Requirements
Setup the Pipeline:

Use OpenAI or Gemini API to process raw, unstructured text data into structured JSON output with the following fields:
field_1, field_2, field_3.
Design a well-defined prompt to ensure accurate outputs from the API.
Prompt Engineering:

Use Pydantic models to validate the API response structure and ensure data integrity.
Local Model Integration:

Set up a locally hosted LLM (e.g., LLaMA or similar).
Process the same data pipeline using the local model and compare the outputs with those from the external API.
Error Handling:

Handle API failures, rate limits, and invalid responses gracefully.
Deliverable
Pipeline code with prompt engineering and validation scripts.
Comparison report of outputs from the external API and the locally hosted model.
# Part 3: Metrics Extraction and Automation from SQL
Database Schema
```sql
Copy code
CREATE TABLE search_clicks (
  search_id SERIAL PRIMARY KEY,
  search_query VARCHAR(255),
  clicks INT DEFAULT 0,
  impressions INT DEFAULT 0,
  click_through_rate FLOAT,
  search_date DATE DEFAULT CURRENT_DATE
);
```
Requirements
Metrics Analysis: Write SQL queries to analyze the search_clicks data.

Calculate the average click-through rate (CTR) for each day.
Identify the top 5 search queries with the highest CTR over a given period.
Detect queries with high impressions but low clicks (possible optimization candidates).
Pipeline Automation:

Develop a Python script to execute these SQL queries and store the results in a search_insights summary table:
```sql
Copy code
CREATE TABLE search_insights (
  id SERIAL PRIMARY KEY,
  insight_date DATE,
  average_ctr FLOAT,
  top_queries JSONB,
  low_performance_queries JSONB
);
```
Automate the script to run daily using a scheduler like cron or Celery.
Deliverable
SQL queries and the summary table structure.
Python script for pipeline automation.
Sample output of the pipeline with mock data.
Use Supabase Free Tier for the Assignment
To complete this assignment, use Supabase free tier for database hosting. Supabase offers PostgreSQL database hosting with an easy-to-use API for backend development.

Example Database Structure
You can use the schema provided above and create the users, orders, and search_clicks tables in your Supabase project.

Dummy Dataset Creation
For testing purposes, generate a dummy dataset that mimics the real data for each of the three parts of the project.

Submission Instructions
Create a GitHub repository or zip file containing the following:

Full API implementation (including FastAPI code, test cases, and any necessary dependencies).
The data processing pipeline with OpenAI or Gemini integration and comparison results with the locally hosted model.
SQL queries, the summary table structure, and Python script for the automated metrics pipeline.
Sample output with mock data for each part.


