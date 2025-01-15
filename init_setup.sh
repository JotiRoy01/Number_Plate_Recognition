

# echo [$(date)]: "START"
# export _VERSION_= 3.10
# echo [$(date)]: "Creating Environment With Python $(_VERSION_)"
# conda create --prefix ./env_number_plate python=$(_VERSION_) -y
# echo [$(date)]: "Activate Virtual Environment"
# source activate D:\Develops\MLOPS\Number_Plate_Recognition\env_number_plate
# echo[$(data)] "Export Conda Environment"


# # echo [$(date)] "Install All Requirement"
# # pip install requirements.txt

# Bash shell script to create the directory structure and __init__.py files

# Define the base directory
BASE_DIR="src/ANPR"

# List of subdirectories to create
DIRECTORIES=(
    "components"
    "config"
    "constants"
    "entity"
    "exception"
    "logger"
    "pipeline"
    "utils"
)

# Loop through each directory and create it along with __init__.py
for DIR in "${DIRECTORIES[@]}"
do
    # Create the full directory path
    FULL_PATH="$BASE_DIR/$DIR"
    echo "[$(date)]: Creating $FULL_PATH"

    # Create the directory (including parents if necessary)
    mkdir -p "$FULL_PATH"

    # Create the __init__.py file
    INIT_FILE="$FULL_PATH/__init__.py"
    echo "[$(date)]: Creating __init__.py inside $FULL_PATH"

    # Add a placeholder comment to the __init__.py file
    echo "# __init__.py for $DIR" > "$INIT_FILE"
done

# echo [$(date)] "Install All Requirement"
# pip install -r requirements.txt