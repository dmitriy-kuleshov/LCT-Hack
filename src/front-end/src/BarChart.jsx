import React, { useState, useEffect, useRef } from 'react'
import * as d3 from 'd3'
import { sv } from 'date-fns/locale'

const { select, line, curveCardinal, scaleLinear, axisBottom, axisLeft } = d3

const makeChart = (dataset, svg) => {
  console.log(dataset)
  const width = 640
  const height = 400
  const marginTop = 30
  const marginRight = 20
  const marginBottom = 30
  const marginLeft = 20
  const paddingTop = 10
  const paddingLeft = 50

  dataset.sort((a, b) => b.amount - a.amount)

  svg
    .attr('viewBox', [0, 0, width, height])
    .attr('width', width + marginLeft + marginRight)
    .attr('height', height + marginTop + marginBottom)
    .attr('transform', 'translate(' + marginLeft + ',' + marginTop + ')')

  const x = d3
    .scaleLinear()
    .domain([0, Math.max(...dataset.map(({ amount }) => amount))])
    .range([0, width - paddingLeft])
  const y = d3
    .scaleBand()
    .domain(dataset.map(({ name }) => name))
    .range([0, height - paddingTop])

  svg
    .append('g')
    .call(d3.axisTop(x))
    .attr('transform', `translate(${paddingLeft},${paddingTop})`)
  svg
    .append('g')
    .attr('transform', `translate(${paddingLeft},${paddingTop})`)
    .call(d3.axisLeft(y))

  svg
    .append('g')
    .attr('transform', `translate(${paddingLeft},${paddingTop})`)
    .attr('fill', 'steelblue')
    .selectAll()
    .data(dataset)
    .join('rect')
    .attr('x', (d) => x(0))
    .attr('y', (d) => y(d.name))
    .attr('width', (d) => x(d.amount) - x(0))
    .attr('height', y.bandwidth() / 2)
    .attr('transform', 'translate(' + 0 + ',' + y.bandwidth() / 4 + ')')
}

const random = () => Math.round(Math.random() * 100)

const data = [
  { name: `Тест ${random()}`, amount: random() },
  { name: `Тест ${random()}`, amount: random() },
  { name: `Тест ${random()}`, amount: random() },
  { name: `Тест ${random()}`, amount: random() },
  { name: `Тест ${random()}`, amount: random() },
]

// const max = dataset
//   .map(({ amount }) => amount)
//   .reduce((acc, i) => Math.max(acc, i), 0)

const BarChart = () => {
  //refs
  const svgRef = useRef()

  //draws chart
  useEffect(() => {
    const svg = select(svgRef.current)
    makeChart(data, svg)
  }, [data])

  return <svg ref={svgRef}></svg>
}
export default BarChart
