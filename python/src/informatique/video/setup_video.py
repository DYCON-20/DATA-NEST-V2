import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from datetime import datetime, timedelta
from Setting.setting import  Theme
def setup():
    try:
        print("-")
        print("🟦 Prepare the different files for the final video [ B{2/10} ]🟦")
        datetime_Monitoring = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
        print("setup")
        base_path = "./python/data"
        nested_dirs = [f"Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/video",
                    f"Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/subtitle",
                    f"Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/final_component",
                    f"Monitoring/{Theme}/{Theme}_monitoring_{datetime_Monitoring}/audio"]
        for dir_path in nested_dirs:
            full_path = os.path.join(base_path, dir_path)
            os.makedirs(full_path, exist_ok=True)
        created_dirs = [os.path.isdir(os.path.join(base_path, dir_path)) for dir_path in nested_dirs]
        created_dirs
    except Exception as e:
            print(f"""❌❌An error has occurred() ❌❌
            ➡️Here is the error message 🟨{e}🟨 """)

