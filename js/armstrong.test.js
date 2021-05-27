// const { expect } = require('@jest/globals');
// const { test } = require('jest-circus');

let h = require('./armstrongNumbers');
//const arm  = require('./armstrongNumbersSpec');

function createArrayOfNum(maxValue) {
  return Array.apply(null, {length: maxValue}).map(Number.call, Number)
}

test('array of size 80', () => {
  expect(h(createArrayOfNum(80))).toEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]);
})

test('array of size 8', () => {
  expect(h(createArrayOfNum(8))).toEqual([0, 1, 2, 3, 4, 5, 6, 7]);
})

test('array of size 10', () => {
  expect(h(createArrayOfNum(10))).toEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]);
})

test('array of size 80', () => {
  expect(h(createArrayOfNum(999))).toEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]);
})