function binarySearch(arr, target) {
  let low = 0;
  let high = arr.length - 1;

  while (low <= high) {
    const middle = Math.floor((low + high) / 2);
    const guess = arr[middle];

    if (guess === target) {
      return middle;
    }

    if (guess > target) {
      high = high - 1;
    } else {
      low = low + 1;
    }
  }
}
