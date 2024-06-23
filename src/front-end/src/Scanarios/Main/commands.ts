import {
  getAmountFromServer,
  getForecastFromServer,
  getPurchaseFromServer,
} from '../../services'
import { jsonToBlob } from '../../utils/jsonToBlob'
import { makeLinkFromBlob } from '../../utils/makeLinkFromBlob'
import { makeMessageText } from '../../utils/makeMessageText'
import { Command, CommandsTypes } from '../types'
import { MainNodeNames } from './types'

export const goTo = (
  name: string,
  node: MainNodeNames
): Command<MainNodeNames> => ({
  type: CommandsTypes.changeNode,
  name,
  to: node,
})

export const goToWithMessage = (
  message: string,
  node: MainNodeNames
): Command<MainNodeNames> => ({
  name: 'Переход',
  type: CommandsTypes.changeNodeWithMsg,
  message,
  to: node,
})

export const goBack = (back: MainNodeNames) => goTo('Назад', back)

export const goToAmount = goTo(
  'Посмотреть остатки',
  MainNodeNames.amountGetDate
)

export const goToForecast = goTo(
  'Получить прогноз',
  MainNodeNames.forecastGetProducts
)

export const goToPurchase = goTo(
  'Получить файл заявки',
  MainNodeNames.purchaseResult
)

export const getAmount: Command<MainNodeNames> = {
  name: 'Получить остаток',
  type: CommandsTypes.async,
  message: 'Загружаем данные...',
  callback: async ({ amountDate, amountProducts }) => {
    try {
      const data = await getAmountFromServer(amountProducts, amountDate)
      const answer = `Остатки товаров ${amountDate}:\n\n${makeMessageText(data, ({ name, amount }: any) => `${name} - ${amount} шт`)}`
      return goToWithMessage(answer, MainNodeNames.start)
    } catch {
      return goToWithMessage(
        'Произошла ошибка, попробуйте позже',
        MainNodeNames.start
      )
    }
  },
}

export const getForecast: Command<MainNodeNames> = {
  name: 'Получить прогноз',
  type: CommandsTypes.async,
  message: 'Загружаем данные...',
  callback: async ({ forecastProducts }) => {
    try {
      const data = await getForecastFromServer(forecastProducts)
      const answer = `Прогноз:\n\n${makeMessageText(data, ({ name, date }: any) => `${name} закончится ${date}`)}`
      return goToWithMessage(answer, MainNodeNames.start)
    } catch {
      return goToWithMessage(
        'Произошла ошибка, попробуйте позже',
        MainNodeNames.start
      )
    }
  },
}

export const getPurchase: Command<MainNodeNames> = {
  name: 'Получить файл',
  type: CommandsTypes.async,
  message: 'Загружаем данные...',
  callback: async () => {
    try {
      const data = await getPurchaseFromServer()
      const blob = jsonToBlob(data)
      const link = makeLinkFromBlob(blob)

      return {
        type: CommandsTypes.sendFile,
        name: 'Отправка файла',
        link,
        to: MainNodeNames.start,
      }
    } catch {
      return goToWithMessage(
        'Произошла ошибка, попробуйте позже',
        MainNodeNames.start
      )
    }
  },
}
