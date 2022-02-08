import React, { Component } from 'react'
import './App.css'
import { scaleLinear, scaleBand } from 'd3-scale'
import { axisBottom, axisLeft } from 'd3-axis'
import { select } from 'd3-selection'

class BarChart extends Component {
    constructor(props) {
        super(props)
        this.createBarChart = this.createBarChart.bind(this)
    }

    componentDidMount() {
        this.createBarChart()
    }

    componentDidUpdate() {
        this.createBarChart()
    }

    createBarChart() {
        const node = this.node
        const dataMax = 20
        const yScale = scaleLinear()
            .domain([0, dataMax]) // Gives a range to the values to expect for the height
            .range([this.props.size[1], 0]) // Controls the height of the bars

        var xDomain = []
        var label = 1

        for (var x of this.props.data) {
            xDomain.push(label)
            label++
        }

        const xScale = scaleBand()
            .domain(xDomain)
            .range([0, xDomain.length*20])

        const xAxis = axisBottom(xScale)
        const yAxis = axisLeft(yScale)

        select(node)
            .selectAll('rect')
            .data(this.props.data)
            .enter()
            .append('rect')

        select(node)
            .selectAll('rect')
            .data(this.props.data)
            .exit()
            .remove()

        // var chartGroup = select(node)
        //                     .append('g')
        //                     .attr('transform', 'translate(20, 20)')

        select(node)
            .selectAll('rect')
            .data(this.props.data)
            .style('fill', '#000000')
            .attr('x', (d, i) => i*20)
            .attr('y', d => yScale(d.Value))
            .attr('height', d => this.props.size[1] - yScale(d.Value))
            .attr('width', 15)
            .attr('transform', 'translate(20, 20)')

        select(node)
            .append('g')
            .attr('class', 'x axis hidden')
            .attr('transform', 'translate(20, 320)')
            .call(xAxis)

        select(node)
            .append('g')
            .attr('class', 'y axis')
            .attr('transform', 'translate(20, 20)')
            .call(yAxis)

    }

    render() {
        return <svg ref={node => this.node = node}
        width={1000} height={400}>
        </svg>
    }
}
export default BarChart
