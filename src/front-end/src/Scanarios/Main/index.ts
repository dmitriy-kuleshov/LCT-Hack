import { Scenario } from '../types'
import {
  AmountGetDate,
  AmountGetProducts,
  AmountResult,
  ForecastGetProducts,
  ForecastResult,
  PurchaseResult,
  Start,
} from './nodes'
import { MainNodeNames } from './types'

export const MainScenario: Scenario<MainNodeNames> = {
  [MainNodeNames.start]: Start,
  [MainNodeNames.amountGetDate]: AmountGetDate,
  [MainNodeNames.amountGetProducts]: AmountGetProducts,
  [MainNodeNames.amountResult]: AmountResult,
  [MainNodeNames.forecastGetProducts]: ForecastGetProducts,
  [MainNodeNames.forecastResult]: ForecastResult,
  [MainNodeNames.purchaseResult]: PurchaseResult,
}
