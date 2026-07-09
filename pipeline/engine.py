import pandas as pd

class AnalyticsEngine:
    @staticmethod
    def process_large_scale_dataset(filepath="data/mock_records.csv"):
        """Loads large-scale datasets from file storage and aggregates values."""
        try:
            df = pd.read_csv(filepath)
            
            # Feature extraction processing
            df['is_cross_functional'] = df['department'].str.contains('Cross-Functional')
            
            # High-speed data grouping operations
            summary = df.groupby('is_cross_functional')['projects_completed'].agg(['sum', 'mean', 'count'])
            summary.index = ['Functional Teams', 'Cross-Functional Teams']
            
            print("\n" + "="*35)
            print("   SCALED DATA ANALYTICS REPORT   ")
            print("="*35)
            print(summary)
            print("="*35)
            
        except FileNotFoundError:
            print(f"Processing Error: Source file '{filepath}' could not be located.")
