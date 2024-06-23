import { FromTypes } from '../Message'
import { TestNodesNames } from '../Scanarios/TestScenario/commands'

export const appReducer = (Scenario) => (state, action) => {
  //console.log(state)
  switch (action.type) {
    case ActionTypes.addMessage: {
      // console.log('add mes')
      const { text, from } = action.payload
      const { messages } = state
      return { ...state, messages: [...messages, { text, from }] }
    }
    case ActionTypes.changeNode: {
      const { to } = action.payload
      //console.log(to)
      return {
        ...state,
        currentNode: to,
        currentCommands: Scenario[to].commands,
        messages: [
          ...state.messages,
          { from: FromTypes.bot, text: Scenario[to].message },
        ],
      }
    }
    case ActionTypes.sendFile: {
      const { link } = action.payload
      console.log('reducer', link)
      //console.log(to)
      return {
        ...state,
        messages: [
          ...state.messages,
          { from: FromTypes.bot, link, type: 'file' },
        ],
      }
    }
    default: {
      return state
    }
  }
}

export const ActionTypes = {
  addMessage: 'addMessage',
  changeNode: 'changeNode',
  changeNodeWithMsg: 'changeNodeWithMsg',
  sendFile: 'sendFile',
}

export const AppInitState = (Scenario, currentNode) => ({
  messages: [{ from: FromTypes.bot, text: 'Выберите команду' }],
  currentNode,
  currentCommands: Scenario[currentNode].commands,
})

const messageFromBot = (msg) => ({
  type: ActionTypes.addMessage,
  payload: { from: FromTypes.bot, text: msg },
})

const messageFromUser = (msg) => ({
  type: ActionTypes.addMessage,
  payload: { from: FromTypes.user, text: msg },
})

const changeNode = (node) => ({
  type: ActionTypes.changeNode,
  payload: { to: node },
})

const sendFile = (link) => ({
  type: ActionTypes.sendFile,
  payload: {
    link,
  },
})

export const appActions = {
  messageFromBot,
  messageFromUser,
  changeNode,
  sendFile,
}
