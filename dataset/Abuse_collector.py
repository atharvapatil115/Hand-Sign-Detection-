from DataSet_collector import DataCollector
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

DataCollector = DataCollector("Fuck You","Abuse",max_samples=100)

DataCollector.collect()