const unsorted = [5, 1, 8, 4, 9, 6, 2, 7, 3]

const merge = (arr1, arr2) => {
  const sorted = []
  while (arr1.length && arr2.length) {
    if (arr1[0] < arr2[0]) sorted.push(arr1.shift())
    else sorted.push(arr2.shift())
  }
  return sorted.concat(arr1.slice().concat(arr2.slice()))
}

const mergeSort = (arr) => {
  if (arr.length <= 1) return arr

  const mid = Math.floor(arr.length / 2)
  const left = mergeSort(arr.slice(0, mid))
  const right = mergeSort(arr.slice(mid))
  return merge(left, right)
}

console.log(mergeSort(unsorted).join(' ')) // Invoking Sort
