import os

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from datetime import datetime, timedelta

from Setting.setting import  Theme




def setup():
    print("-")
    print("🟦 Prepare the different files for the final video [ B{2/10} ]🟦")
    
    datetime_Monitoring = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    print("setup")



    # Define the base directory path
    base_path = "./python/data"

    # Define the nested directory structure
    nested_dirs = [f"Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/video",
                f"Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/subtitle",
                f"Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/final_component",
                f"Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/audio"]

    # Create the nested directories if they do not exist
    for dir_path in nested_dirs:
        full_path = os.path.join(base_path, dir_path)
        os.makedirs(full_path, exist_ok=True)

    # Check if the directories were created successfully
    created_dirs = [os.path.isdir(os.path.join(base_path, dir_path)) for dir_path in nested_dirs]
    created_dirs
    pass