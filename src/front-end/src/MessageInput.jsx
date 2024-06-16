import React, { useRef } from 'react'
import styled from 'styled-components'
import CommandPalette from './CommandPalette'
import useInput from './useInput'
import Icon from './assets/icons8-send-60.png'

const MessageInputHeight = '50px'

const Input = styled.input`
  width: 100%;
  height: ${MessageInputHeight};
  -webkit-text-size-adjust: 100%;
  -webkit-font-smoothing: antialiased;
  --body-bg-color: #e5ecef;
  --theme-bg-color: #fff;
  --settings-icon-hover: #9fa7ac;
  --developer-color: #f9fafb;
  --input-bg: #f8f8fa;
  --input-chat-color: #a2a2a2;
  --border-color: #eef2f4;
  --body-font: 'Manrope', sans-serif;
  --body-color: #273346;
  --settings-icon-color: #c1c7cd;
  --msg-message: #969eaa;
  --chat-text-bg: #f1f2f6;
  --theme-color: #0086ff;
  --msg-date: #c0c7d2;
  --button-bg-color: #f0f7ff;
  --button-color: var(--theme-color);
  --detail-font-color: #919ca2;
  --msg-hover-bg: rgba(238, 242, 244, 0.4);
  --active-conversation-bg: linear-gradient(
    to right,
    rgba(238, 242, 244, 0.4) 0%,
    rgba(238, 242, 244, 0) 100%
  );
  --overlay-bg: linear-gradient(
    to bottom,
    rgba(255, 255, 255, 0) 0%,
    rgba(255, 255, 255, 1) 65%,
    rgba(255, 255, 255, 1) 100%
  );
  --chat-header-bg: linear-gradient(
    to bottom,
    rgba(255, 255, 255, 1) 0%,
    rgba(255, 255, 255, 1) 78%,
    rgba(255, 255, 255, 0) 100%
  );
  outline: none;
  box-sizing: border-box;
  overflow: visible;
  font-family: sans-serif;
  line-height: 1.15;
  border: none;
  color: var(--body-color);
  background-color: var(--input-bg);
  padding: 12px;
  border-radius: 6px;
  font-size: 15px;
  margin: 0 12px;
  width: 100%;
`

const Container = styled.div`
  position: relative;
  display: flex;
  flex-direction: row;
`

const Button = styled.button`
  border: 0;
  padding: 0;
  height: ${MessageInputHeight};
  width: ${MessageInputHeight};
  border-radius: 50%;
  background-color: #f8f8fa;
  display: flex;
  justify-content: center;
  align-items: center;
`

const MessageInput = ({
  dispatchMessage,
  dispatchCommand: dispatchCommand,
  commands,
  disabledInput,
}) => {
  const [input, onChange, clearInput] = useInput('')

  const sendMessage = () => {
    dispatchMessage(input)
    clearInput()
  }

  return (
    <Container>
      <CommandPalette dispatchCommand={dispatchCommand} commands={commands} />
      <Input
        value={input}
        onChange={onChange}
        onKeyDown={(e) => (e.key === 'Enter' ? sendMessage() : null)}
      />
      <Button onClick={sendMessage}>
        <img src={Icon} width={25} />
      </Button>
    </Container>
  )
}

export default MessageInput
