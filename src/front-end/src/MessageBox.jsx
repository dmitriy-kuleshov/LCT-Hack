import { forwardRef } from 'react'
import styled, { css } from 'styled-components'

// const Right = css`
//   margin-left: auto;
// `

// const Left = css`
//   margin-right: auto;
// `

const Container = styled.div`
  display: flex;
  flex-direction: column;
  background-color: white;
  min-width: 100px;
  width: fit-content;
  padding: 10px;
  border-radius: 10px;
  white-space: pre-wrap;

  ${({ position }) => (position === 'left' ? Left : Right)}/* ${({ styling }) =>
    styling} */
`

const Right = css`
  margin-left: auto;
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
  padding: 15px;
  line-height: 1.5;
  font-size: 14px;
  font-weight: 500;
  background-color: var(--theme-color);
  color: #fff;
  border-radius: 20px 20px 0 20px;
`

const Left = css`
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

const Title = styled.span`
  font-size: 16px;
  font-weight: bold;
`

const Text = styled.p`
  font-size: 18px;
`

const MessageBox = ({ text, title, position }, ref) => {
  return (
    <Container position={position}>
      {/* <Title>{title}</Title> */}
      {text}
    </Container>
  )
}

export default MessageBox
