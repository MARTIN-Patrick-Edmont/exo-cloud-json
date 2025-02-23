import azure.functions as func
import logging
import re
import json
app = func.FunctionApp()

@app.blob_trigger(arg_name=[BLOB_NAME], path=[BLOB_PATH],
                               connection=[STORAGE ACCOUNT]) 
def exojson([BLOB_NAME]: func.InputStream):
    logging.info(f"Python blob trigger function processed blob"
                f"Name: {myblob.name}"
                f"Blob Size: {myblob.length} bytes")
    [BLOB_NAME].name.match(r".*(\.json)$")
    if re.match(r".*(.json)\Z"): # Is it a .json ?
        try : json.load([BLOB_NAME]) # Is it a *good* json ?
        except: logging.error("JSON failed to decode")
    else:
        logging.error("The file submitted was not a JSON file.")
