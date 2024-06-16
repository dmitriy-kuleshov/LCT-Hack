import React, { useEffect, useRef } from 'react'
import { MessageBox } from 'react-chat-elements'
import styled from 'styled-components'
import Message from './Message'
import MesseageFile from './MessageFile'

const Container = styled.div`
  gap: 10px;
  display: flex;
  flex-direction: column;
  overflow-y: scroll;
  padding: 10px;
  padding-bottom: 50px;

  &::-webkit-scrollbar {
    width: 0px;
    background: transparent; /* make scrollbar transparent */
  }
`

const MessageList = ({ data }) => {
  const lastRef = useRef()
  //const executeScroll = () => lastRef.current.scrollIntoView()
  useEffect(() => {
    lastRef.current.scrollIntoView({ behavior: 'smooth' })
  }, [data])

  return (
    <Container>
      {data.map(({ from, type, text, ...payload }, index) => (
        <Message key={index} type={type} from={from} text={text} {...payload} />
      ))}
      {/* <MesseageFile name="Файл закупки" /> */}
      <div ref={lastRef} />
    </Container>
  )
}

export default MessageList
