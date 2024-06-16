import { isValid, parse } from 'date-fns'

const validateByFormat = (input, format) => {
  //console.log(parse(input, format))
  return isValid(parse(input, format, new Date()))
}

export const validateDate = (input) => {
  return validateByFormat(input, 'dd.mm.yyyy')
}
