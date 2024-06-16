export const getAmountFromServer = async (prodcuts, date) => {
  console.log('getAmountFromServer', prodcuts, date)
  return [
    {
      name: 'Печь СВЧ SUPRA MWS-2117MW, 21л., 700Вт., белый',
      amount: '5',
    },
    {
      name: 'Микроволновая печь SAMSUNG ME83XR/BWT, мощность 800 Вт, черная',
      amount: '5',
    },
    {
      name: 'Огнетушитель порошковый ОП-5 (з) (АВСЕ)',
      amount: '5',
    },
  ]
}

export const getForecastFromServer = async (prodcuts) => {
  return [
    {
      name: 'Печь СВЧ SUPRA MWS-2117MW, 21л., 700Вт., белый',
      date: '12.12.12',
    },
    {
      name: 'Микроволновая печь SAMSUNG ME83XR/BWT, мощность 800 Вт, черная',
      date: '12.12.12',
    },
    {
      name: 'Огнетушитель порошковый ОП-5 (з) (АВСЕ)',
      date: '12.12.12',
    },
  ]
}

export const getPurchaseFromServer = async () => {
  return {
    id: 1, //идетнификатор расчета
    lotEntityId: 1, //Идентификатор лота
    CustomerId: 1, //Идентификатор заказчика
    rows: [
      //Строки спецификации
      {
        DeliverySchedule: {
          //График поставки
          dates: {
            end_date: ' ', //Дата окончания поставки
            start_date: ' ', //Дата начала поставки
          },
          deliveryAmount: 1, //Объем поставки
          deliveryConditions: '', //Условия поставки
          year: 1, //Год
        },
        address: {
          //Адрес поставки
          gar_id: ' ', //Идентификатор ГАР
          text: ' ', //Адрес в текстовой форме
        },
        entityId: 1, //Сквозной идентификатор СПГЗ
        id: 1, //Идентификатор (версии) СПГЗ
        nmc: 1, //Сумма спецификации
        okei_code: ' ', //Ед. измерения по ОКЕИ
        purchaseAmount: 1, //Объем поставки
        spgzCharacteristics: [
          //Характеристики СПГЗ. Заполняются в зависимости от типа характеристики в соответствии со структурой справочника СПГЗ
          {
            characteristicName: ' ',
            characteristicSpgzEnums: [{ value: ' ' }],
            conditionTypeId: 1,
            kpgzCharacteristicId: 1,
            okei_id: 1,
            selectType: 1,
            typeId: 1,
            value1: 1,
            value2: 1,
          },
        ],
      },
    ],
  }
}
