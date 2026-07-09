import pandas as pd
import random
import os

class BigDataGenerator:
    @staticmethod
    def generate_and_save(num_records=50000, output_path="data/mock_records.csv"):
        """Synthesizes batch data at scale and saves directly to disk."""
        print(f"Synthesizing {num_records} transaction rows...")
        
        departments = ['Engineering', 'Product Tiger (Cross-Functional)', 'Marketing', 'Sales', 'Launchpad (Cross-Functional)']
        quarters = ['2026-Q1', '2026-Q2', '2026-Q3', '2026-Q4']
        
        data = {
            'emp_id': range(1, num_records + 1),
            'department': [random.choice(departments) for _ in range(num_records)],
            'quarter': [random.choice(quarters) for _ in range(num_records)],
            'projects_completed': [random.randint(1, 15) for _ in range(num_records)]
        }
        
        df = pd.DataFrame(data)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df.to_csv(output_path, index=False)
        print(f"Data batch successfully cached at '{output_path}'.")
