import { forwardRef, useRef } from 'react'
import styled, { css } from 'styled-components'

import Icon from './assets/icons8-file-100.png'
import { makeLinkFromBlob } from './utils/makeLinkFromBlob'
import { jsonToBlob } from './utils/jsonToBlob'

const Container = styled.div`
  display: flex;
  flex-direction: row;
  background-color: white;
  min-width: 100px;
  width: fit-content;
  padding: 10px;
  border-radius: 10px;
  align-items: center;

  margin-right: auto;
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
  font-family: var(--body-font);
  outline: none;
  box-sizing: border-box;
  background-color: var(--chat-text-bg);
  padding: 15px;
  border-radius: 20px 20px 20px 0;
  line-height: 1.5;
  font-size: 14px;
  font-weight: 500;
  color: var(--chat-text-color);
`

const DowloadLink = styled.a`
  display: none;
`

const FileIcon = styled.div`
  --size: 50px;
  border-radius: 50%;
  width: var(--size);
  height: var(--size);
  background-color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-right: 10px;
`

const MesseageFile = ({ name = 'Файл закупки', link }) => {
  //link = makeLinkFromBlob(jsonToBlob({ call: 'call' }))
  console.log(link)
  const linkRef = useRef()
  return (
    <Container>
      <DowloadLink ref={linkRef} href={link} download={name + '.json'} />
      <FileIcon
        onClick={() => {
          linkRef.current?.click()
        }}
      >
        <img width={35} height={35} src={Icon} />
      </FileIcon>
      {/* <Title>{title}</Title> */}
      {name}
    </Container>
  )
}

export default MesseageFile
