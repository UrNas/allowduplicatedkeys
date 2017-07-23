# Allow duplicated keys at dictionary

**requirement python 3.0 or later**

### example 
```python
from allowduplicatedkey import AllowDuplicatedKey

data = AllowDuplicatedKey()
data['name'] = 'python'
data['name'] = 'another value'
# print it as json
data.all_as_json()
# print specific key as json
data.as_json('name')

```





