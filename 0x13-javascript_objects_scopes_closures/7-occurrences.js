#!/usr/bin/node
// Return the number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
  let c = 0;
  for (let i = 0; i < list.length; ++i) {
    if (list[i] === searchElement) {
      ++c;
    }
  }
  return c;
};
