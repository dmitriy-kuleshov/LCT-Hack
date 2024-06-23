import { validateDate } from '../../utils/validation'
import { NodeTypes, ScenarioNode } from '../types'
import {
  getAmount,
  getForecast,
  getPurchase,
  goBack,
  goTo,
  goToAmount,
  goToForecast,
  goToPurchase,
} from './commands'
import { MainNodeNames } from './types'

export const Start: ScenarioNode<MainNodeNames> = {
  type: NodeTypes.BaseNode,
  commands: [goToAmount, goToForecast, goToPurchase],
  message: 'Выберите команду',
}

export const AmountGetDate: ScenarioNode<MainNodeNames> = {
  type: NodeTypes.AnswerNode,
  commands: [goBack(MainNodeNames.start)],
  message: 'Введите дату в формате дд.мм.ггг',
  validation: (input) => validateDate(input),
  answerVar: 'amountDate',
  nextNode: MainNodeNames.amountGetProducts,
  errorMessage: 'Введите дату в формате дд.мм.ггг',
}

export const AmountGetProducts: ScenarioNode<MainNodeNames> = {
  type: NodeTypes.AnswerNode,
  commands: [goBack(MainNodeNames.amountGetDate)],
  message: 'Введите инетересующие товары через запятую',
  validation: () => true,
  answerVar: 'amountProducts',
  nextNode: MainNodeNames.amountResult,
  errorMessage: 'Введите инетересующие товары через запятую',
  processing: (input: string) => {
    return input.split(',').map((item) => item.trim())
  },
}

export const AmountResult: ScenarioNode<MainNodeNames> = {
  type: NodeTypes.ExecuteNode,
  execute: getAmount,
  commands: [],
}

export const ForecastGetProducts: ScenarioNode<MainNodeNames> = {
  type: NodeTypes.AnswerNode,
  commands: [],
  message: 'Введите инетересующие товары через запятую',
  validation: () => true,
  answerVar: 'forecastProducts',
  nextNode: MainNodeNames.forecastResult,
  errorMessage: 'Введите инетересующие товары через запятую',
  processing: (input: string) => {
    return input.split(',').map((item) => item.trim())
  },
}

export const ForecastResult: ScenarioNode<MainNodeNames> = {
  type: NodeTypes.ExecuteNode,
  commands: [],
  execute: getForecast,
}

export const PurchaseResult: ScenarioNode<MainNodeNames> = {
  execute: getPurchase,
  type: NodeTypes.ExecuteNode,
  commands: [],
}
