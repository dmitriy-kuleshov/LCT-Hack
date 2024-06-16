export const makeLinkFromBlob = (blob) => {
  return window.URL.createObjectURL(new Blob([blob]))
}
