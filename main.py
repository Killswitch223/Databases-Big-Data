from pipeline.generator import BigDataGenerator
from pipeline.engine import AnalyticsEngine

def main():
    print("Initializing Corporate Analytics Engine...")
    
    # 1. Run the generation script to output raw data file
    BigDataGenerator.generate_and_save(num_records=60000)
    
    # 2. Trigger the engine to read, parse, and analyze data
    AnalyticsEngine.process_large_scale_dataset()

if __name__ == "__main__":
    main()
