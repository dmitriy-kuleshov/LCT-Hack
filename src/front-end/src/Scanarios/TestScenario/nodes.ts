import { validateDate } from '../../utils/validation'
import { NodeTypes, ScenarioNode } from '../types'
import {
  GoToNode1,
  GoToNode2,
  GoToNode3,
  asyncCommand,
  GoBack,
  TestNodesNames,
  GetDate,
} from './commands'

export const StartNode: ScenarioNode<TestNodesNames> = {
  type: NodeTypes.BaseNode,
  message: 'Выберите этап',
  commands: [GoToNode1, asyncCommand, GetDate],
}

export const Stage1Node: ScenarioNode<TestNodesNames> = {
  type: NodeTypes.BaseNode,
  message: 'Напишите для этапа 1',
  commands: [GoToNode2, GoBack],
}

export const Stage2Node: ScenarioNode<TestNodesNames> = {
  type: NodeTypes.BaseNode,
  message: 'Напишите для этапа 2',
  commands: [GoToNode3, GoBack],
}

export const Stage3Node: ScenarioNode<TestNodesNames> = {
  type: NodeTypes.BaseNode,
  message: 'Напишите для этапа 3',
  commands: [GoToNode1, GoBack],
}

export const DateNode: ScenarioNode<TestNodesNames> = {
  type: NodeTypes.AnswerNode,
  message: 'Ввведите дату в формате dd.mm.yyyy',
  commands: [GoBack],
  validation: (input) => {
    if (validateDate(input)) return true
    return false
  },
  answerVar: 'date',
  errorMessage: 'Введите пожалуйста дату в формате dd.mm.yyyy',
  nextNode: TestNodesNames.start,
}
