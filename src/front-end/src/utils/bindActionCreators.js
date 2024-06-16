export const bindActionCreators = (actions, dispatch) => {
  const ObjectWithDispathedActions = {}
  for (const [key, value] of Object.entries(actions)) {
    ObjectWithDispathedActions[key] = (...args) => dispatch(value(...args))
  }
  return ObjectWithDispathedActions
}
