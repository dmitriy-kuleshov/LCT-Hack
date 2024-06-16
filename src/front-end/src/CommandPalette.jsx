import React from 'react'
import styled from 'styled-components'

const Container = styled.div`
  position: absolute;
  transform: translateY(-100%);
  width: 100%;
  height: fit-content;
  //background-color: black;
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  padding: 10px;
`

const Command = styled.span`
  padding: 8px;
  border-radius: 15px;
  background-color: green;
  color: white;
  font-size: 12px;
`

function shuffle(array) {
  let currentIndex = array.length

  // While there remain elements to shuffle...
  while (currentIndex != 0) {
    // Pick a remaining element...
    let randomIndex = Math.floor(Math.random() * currentIndex)
    currentIndex--

    // And swap it with the current element.
    ;[array[currentIndex], array[randomIndex]] = [
      array[randomIndex],
      array[currentIndex],
    ]
  }

  return array
}

const CommandPalette = ({ dispatchCommand, dispatchMessage, commands }) => {
  return (
    <Container>
      {commands.map((command, index) => (
        <Command
          key={index}
          onClick={() => {
            dispatchCommand(command)
          }}
        >
          {command.name}
        </Command>
      ))}
    </Container>
  )
}

export default CommandPalette
