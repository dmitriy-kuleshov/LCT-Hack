import React from 'react'
import styled from 'styled-components'
import MessageInput from './MessageInput'
import MessageList from './MessageList'
import { FromTypes } from './Message'
import useChatBot from './useChatBot'
import { MainScenario } from './Scanarios/Main'
import { MainNodeNames } from './Scanarios/Main/types'

const DialogWindow = styled.div`
  width: 500px;
  height: 98vh;
  background-color: white;
  margin-left: auto;
  margin-right: auto;
  display: grid;
  grid-template-rows: 1fr 50px;
`

const Dialog = () => {
  const { messages, commands, dispatchCommand, dispatchMessage } = useChatBot(
    MainScenario,
    MainNodeNames.start
  )

  return (
    <DialogWindow>
      <MessageList data={messages ?? []} />
      <MessageInput
        commands={commands}
        dispatchCommand={dispatchCommand}
        dispatchMessage={dispatchMessage}
      />
    </DialogWindow>
  )
}

export default Dialog
