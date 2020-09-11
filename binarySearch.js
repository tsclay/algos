const nums = [
  -2,
  3,
  4,
  7,
  8,
  9,
  11,
  13,
  15,
  17,
  18,
  19,
  20,
  21,
  23,
  24,
  25,
  28,
  30
]

//===========================================================
// LINEAR SEARCH
//===========================================================
/* Assuming that the input array is sorted and has no duplicates */

const linearSearch = (arr, target) => {
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === target) {
      return i
    }
  }
  return -1
}

console.time('Liner: ')
console.log('linear', linearSearch(nums, 19))
console.timeEnd('Liner: ')

//===========================================================
// BINARY SEARCH
//===========================================================
/* Assuming that the input array is sorted and has no duplicates */

// Recursive
const binarySearchRecursive = (
  arr,
  target,
  left = 0,
  right = arr.length - 1
) => {
  if (left > right) return -1
  const mid = Math.floor(left + (right - left) / 2)

  if (arr[mid] === target) {
    return mid
  }
  if (target < arr[mid]) {
    return binarySearchRecursive(arr, target, left, mid - 1)
  }
  return binarySearchRecursive(arr, target, mid + 1, right)
}

console.time('BS Recursion: ')
console.log('recursive', binarySearchRecursive(nums, 19))
console.timeEnd('BS Recursion: ')

// Iterative
const binarySearchIterative = (arr, target) => {
  let left = 0
  let right = arr.length - 1

  while (left <= right) {
    const mid = Math.floor(left + (right - left) / 2)

    if (arr[mid] === target) {
      return mid
    }
    if (target < arr[mid]) {
      right = mid - 1
    } else {
      left = mid + 1
    }
  }
  return -1
}

console.time('BS Iteration: ')
console.log('iterative', binarySearchIterative(nums, 19))
console.timeEnd('BS Iteration: ')
