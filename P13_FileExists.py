from pathlib import Path
from os.path import exists
file_exists = exists("/content/sample_data/california_housing_test.csv")
print(file_exists)
# True

path = Path("/content/sample_data/california_housing_test.csv")
path.is_file()
# False
