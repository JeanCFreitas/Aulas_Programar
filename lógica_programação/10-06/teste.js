const myMap = new Map();
myMap.set('name', 'Alice');
myMap.set('age', 30);
myMap.set('city', 'New York');

for (const [key, value] of myMap) {
  console.log(`Key: ${key}, Value: ${value}`);
}