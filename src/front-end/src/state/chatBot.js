export const chatBotInitState = {}

const ActionTypes = {
  addVar: 'addVar',
}

export const chatBotReducer = (state, { type, payload }) => {
  console.log(state)
  switch (type) {
    case ActionTypes.addVar: {
      const { name, value } = payload
      return { ...state, [name]: value }
    }
    default: {
      return state
    }
  }
}

const addVariable = (name, value) => ({
  type: ActionTypes.addVar,
  payload: {
    name,
    value,
  },
})

export const chatBotActions = {
  addVariable,
}
