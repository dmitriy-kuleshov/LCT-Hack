import { useState } from 'react'

const useInput = (value, clearValue = value) => {
  const [state, setState] = useState(value)
  const onChange = (e) => {
    setState(e.target.value)
  }
  const clear = () => {
    setState(clearValue)
  }
  return [state, onChange, clear, setState]
}

export default useInput
