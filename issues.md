# issues might occur

### Get fake images file issues:
   
  1. On get fake images file you migh get error :
      "requests.exceptions.InvalidURL: Failed to parse: https://thispersondoesnotexist.com/image"

      ***to solve this***:
      ```python -m pip install --upgrade urllib3```

      or just download requests version 2.21.0

      ```pip uninstall requests # to remove current version
      pip install requests==2.21.0```