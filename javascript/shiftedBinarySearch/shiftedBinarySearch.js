/*
Sample array => [-2, 3, 4, 7, 8, 9, 11, 13]

but it could be given in a shifted form => 
--- [8, 9, 11, 13, -2, 3, 4, 7]
--- [13, -2, 3, 4, 7, 8, 9, 11]
--- [3, 4, 7, 8, 9, 11, 13, -2]
--- so on...

should be solved in 0(log n) time complexity

input array is read-only
*/

const shiftedBinarySearch = (arr, target) => {
  let left = 0
  let right = arr.length - 1

  while (left <= right) {
    const mid = Math.floor(left + (right - left) / 2)

    if (target === arr[mid]) {
      return mid
    }
    if (target === arr[left]) {
      return left
    }
    if (target === arr[right]) {
      return right
    }

    if (arr[left] > arr[right]) {
      if (
        (target > arr[left] && arr[mid] < arr[right] && target > arr[mid]) ||
        (target > arr[left] && arr[mid] > arr[right] && target < arr[mid]) ||
        (target < arr[left] && arr[mid] < arr[right] && target < arr[mid])
      ) {
        right = mid - 1
      } else {
        left = mid + 1
      }
    } else if (target > arr[mid]) {
      left = mid + 1
    } else {
      right = mid - 1
    }

    // if (arr[mid] > arr[mid + 1] && target > arr[right]) {
    //   right = mid - 1
    // } else if (arr[mid] > arr[mid + 1] && target < arr[right]) {
    //   left = mid + 1
    // } else if (target > arr[mid] && target < arr[left]) {
    //   left = mid + 1
    // } else {
    //   right = mid - 1
    // }
  }

  return -1
}

module.exports = shiftedBinarySearch
