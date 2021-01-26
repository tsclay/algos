/* eslint-disable no-undef */
const shiftedBinarySearch = require('../shiftedBinarySearch')

test('finds 13 @ index 0', () => {
  expect(shiftedBinarySearch([13, -2, 3, 4, 7, 8, 9, 11], 7)).not.toBe(-1)
})
test('finds 13 @ index 1', () => {
  expect(shiftedBinarySearch([11, 13, -2, 3, 4, 7, 8, 9], 7)).not.toBe(-1)
})
test('finds 13 @ index 2', () => {
  expect(shiftedBinarySearch([9, 11, 13, -2, 3, 4, 7, 8], 7)).not.toBe(-1)
})
test('finds 13 @ index 3', () => {
  expect(shiftedBinarySearch([8, 9, 11, 13, -2, 3, 4, 7], 7)).not.toBe(-1)
})
test('finds 13 @ index 4', () => {
  expect(shiftedBinarySearch([7, 8, 9, 11, 13, -2, 3, 4], 7)).not.toBe(-1)
})
test('finds 13 @ index 5', () => {
  expect(shiftedBinarySearch([4, 7, 8, 9, 11, 13, -2, 3], 7)).not.toBe(-1)
})
test('finds 13 @ index 6', () => {
  expect(shiftedBinarySearch([3, 4, 7, 8, 9, 11, 13, -2], 7)).not.toBe(-1)
})
test('finds 13 @ index 7', () => {
  expect(shiftedBinarySearch([-2, 3, 4, 7, 8, 9, 11, 13], 7)).not.toBe(-1)
})
