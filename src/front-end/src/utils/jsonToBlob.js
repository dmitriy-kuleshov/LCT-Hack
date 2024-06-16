export const jsonToBlob = (json) => {
  const str = JSON.stringify(json)
  const bytes = new TextEncoder().encode(str)
  const blob = new Blob([bytes], {
    type: 'application/json;charset=utf-8',
  })

  return blob
}
