# Simple LRU Cache

In-memory cache that deletes Least-Recently-Used items when limit is reached

## Prerequisites

python>=2.7

## Usage

```
from lruCache import LruCache

limit = 3
myCache = LruCache(limit)

myCache.set('first', 1)
myCache.set('second', 2)
myCache.set('third', 3)

myCache.get('first') # 1

myCache.set('fourth', 4) # Pushes first entry out of the cache

myCache.get('first') # None
```
