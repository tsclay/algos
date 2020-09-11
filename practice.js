//===========================================================
// Reproduce binary search

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

const indexOf = (arr, target) => {
  let left = 0
  let right = arr.length - 1

  while (left <= right) {
    const mid = Math.floor(left + (right - left) / 2)
    if (arr[mid] === target) return mid
    if (arr[mid] < target) left = mid + 1
    else right = mid - 1
  }

  return -1
}

console.time('algo time')
console.log(indexOf(nums, 30))
console.timeEnd('algo time')
