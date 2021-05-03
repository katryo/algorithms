interface ListNode {
  next?: ListNode;
  prev?: ListNode;
  value: number;
  key: number;
  isDummy: boolean;
}

interface CacheTable {
  [key: number]: ListNode;
}

interface MyCache {
  head: ListNode;
  tail: ListNode;
  capacity: number;
  table: CacheTable;
}

const DUMMY_NODE = { value: 0, isDummy: true, key: 0 };

const updateCacheNode = ({ cache, key }: { cache: MyCache; key: number }) => {
  if (!(key in cache.table)) {
    throw new Error(`${key} not in cache.`);
  }
  const node = cache.table[key];
  if (cache.head === node) {
    return;
  }
  if (cache.tail === node) {
    cache.tail = node.prev;
    cache.tail.next = undefined;
  }
  cache.head.prev = node;
  node.next = cache.head;
  node.prev = undefined;
  cache.head = node;
};

const deleteLeastRecentNode = (cache: MyCache) => {
  if (cache.head === DUMMY_NODE) {
    throw new Error(`Cache does not have objects`);
  }

  const tailNode = cache.tail;
  delete cache.table[tailNode.key];
  if (Object.keys(cache.table).length === 1) {
    cache.head = DUMMY_NODE;
    cache.tail = DUMMY_NODE;
    return;
  }

  tailNode.prev && (tailNode.prev.next = tailNode.next);
  tailNode.next && (tailNode.next.prev = tailNode.prev);
};

const createLruCache = (capacity: number): MyCache => {
  return {
    capacity,
    head: DUMMY_NODE,
    tail: DUMMY_NODE,
    table: {},
  };
};

const getFromCache = ({ cache, key }: { cache: MyCache; key: number }) => {
  if (key in cache.table) {
    updateCacheNode({ cache, key });
    return cache.table[key].value;
  } else {
    console.log(`${key} is not in the cache`);
  }
};

const putToCache = ({
  cache,
  key,
  value,
}: {
  cache: MyCache;
  key: number;
  value: number;
}) => {
  if (key in cache.table) {
    const nodeToBeUpdated = cache.table[key];
    nodeToBeUpdated.value = value;
    updateCacheNode({ cache, key });
    return;
  }

  const newNode: ListNode = { value, isDummy: false, key };
  cache.table[key] = newNode;
  if (cache.head === DUMMY_NODE) {
    cache.tail = newNode;
    cache.head = newNode;
    return;
  }

  cache.head.prev = newNode;
  newNode.next = cache.head;
  cache.head = newNode;

  if (Object.keys(cache.table).length > cache.capacity) {
    deleteLeastRecentNode(cache);
  }
};

const cache = createLruCache(2);
putToCache({ cache, key: 1, value: 10 });
putToCache({ cache, key: 2, value: 20 });
console.log(getFromCache({ cache, key: 1 }));
console.log(getFromCache({ cache, key: 2 }));
putToCache({ cache, key: 3, value: 30 });
console.log(getFromCache({ cache, key: 1 }));
console.log(getFromCache({ cache, key: 2 }));
console.log(getFromCache({ cache, key: 3 }));
