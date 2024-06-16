export const makeMessageText = (array, fn) => {
  return array.reduce((acc, item) => {
    return '' + acc + fn(item) + '\n'
  }, '')
}
