import psycopg2
import json
from datetime import datetime
import schedule
import time

# Database URL
DATABASE_URL = "postgresql://postgres:1234@localhost:5433/assign"

def run_pipeline():
    try:
        # Connect to the PostgreSQL database using the DATABASE_URL
        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()
        print("Connected to the database.")

        # Queries
        print("Executing Average CTR Query...")
        average_ctr_query = """
        SELECT 
            CURRENT_DATE AS insight_date,
            AVG(click_through_rate) AS average_ctr
        FROM 
            search_clicks;
        """
        cursor.execute(average_ctr_query)
        average_ctr_result = cursor.fetchone()
        average_ctr = average_ctr_result[1] if average_ctr_result and average_ctr_result[1] else 0
        print(f"Average CTR: {average_ctr}")

        print("Executing Top Queries Query...")
        top_queries_query = """
        SELECT 
            search_query, 
            click_through_rate
        FROM 
            search_clicks
        WHERE 
            search_date BETWEEN '2024-10-01' AND '2024-12-31'
        ORDER BY 
            click_through_rate DESC
        LIMIT 5;
        """
        cursor.execute(top_queries_query)
        top_queries = [{"query": row[0], "ctr": row[1]} for row in cursor.fetchall()]
        print(f"Top Queries: {json.dumps(top_queries, indent=2)}")

        print("Executing Low Performance Queries Query...")
        low_perf_queries_query = """
        SELECT 
            search_query, 
            impressions, 
            clicks
        FROM 
            search_clicks
        WHERE 
            impressions > 100 
            AND clicks < 10;
        """
        cursor.execute(low_perf_queries_query)
        low_perf_queries = [{"query": row[0], "impressions": row[1], "clicks": row[2]} for row in cursor.fetchall()]
        print(f"Low Performance Queries: {json.dumps(low_perf_queries, indent=2)}")

        # Insert results into the summary table
        print("Inserting results into the summary table...")
        insert_query = """
        INSERT INTO search_insights (insight_date, average_ctr, top_queries, low_performance_queries)
        VALUES (%s, %s, %s, %s);
        """
        cursor.execute(insert_query, (
            datetime.now().date(),
            average_ctr,
            json.dumps(top_queries),
            json.dumps(low_perf_queries)
        ))
        conn.commit()
        print("Pipeline executed successfully.")

    except psycopg2.DatabaseError as db_err:
        print(f"Database Error: {db_err}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()
        print("Database connection closed.")

# Schedule the pipeline to run daily
print("Scheduling the pipeline...")
schedule.every().day.at("00:00").do(run_pipeline)

# Keep the script running
# Temporarily call the function directly to test
run_pipeline()

print("Pipeline is scheduled. Waiting to execute...")
while True:
    schedule.run_pending()
    time.sleep(1)
