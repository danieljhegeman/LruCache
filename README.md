# Simple LRU Cache

In-memory cache that deletes Least-Recently-Used items when limit is reached.

## Prerequisites

Python >= 3.0

## Usage and Behavior

Instantiate a cache that will hold up to a user-defined number of items:
```
from lruCache import LruCache

myCache = LruCache(itemLimit=3)
```
Add entries to cache:
```
myCache.set('first', 1) # None
# None<-{'first'=>1}->None

myCache.set('second', 2) # None
# None<-{'second'=>2}-><-{'first'=>1}->None

myCache.set('third', 3) # None
# None<-{'third'=>3}-><-{'second'=>2}-><-{'first'=>1}->None
```
Accessing a value via its key moves it, the most-recently used entry, to the front of the cache:
```
myCache.get('second') # 2
# None<-{'second'=>2}-><-{'third'=>3}-><-{'first'=>1}->None
```
Once the cache reaches its item limit, the least-recently-used entry is discarded:
```
myCache.set('fourth', 4) # None
# None<-{'fourth'=>4}-><-{'second'=>2}-><-{'third'=>3}->None

myCache.get('first') # None
# None<-{'fourth'=>4}-><-{'second'=>2}-><-{'third'=>3}->None

myCache.get('third') # 3
# None<-{'third'=>3}-><-{'fourth'=>4}-><-{'second'=>2}->None
```
Manually remove an entry from the cache:
```
myCache.remove('fourth') # 4
# None<-{'third'=>3}-><-{'second'=>2}->None

myCache.get('fourth') # None
```
