import React, { Component } from 'react'
import './App.css'
import { axisBottom, axisLeft } from 'd3-axis'
import { select } from 'd3-selection'
import { scaleLinear, scaleTime } from 'd3-scale'
import { line } from 'd3-shape'
import { timeParse, timeFormat } from 'd3-time-format'
import { extent } from 'd3-array'

class LineChart extends Component {
    constructor(props) {
        super(props)
        this.createLineChart = this.createLineChart.bind(this)
    }

    componentDidMount() {
        this.createLineChart()
    }

    componentDidUpdate() {
        this.createLineChart()
    }

    createLineChart() {
        const node = this.node

        var parseDate = timeParse('%Y-%m-%d')
        var date = []

        for (var x of this.props.data) {
            date.push(x.date)
        }

        const height = this.props.size[1]
        const width = this.props.size[0]

        const yScale = scaleLinear()
            .domain([0, height])
            .range([height, 0])

        const xScale = scaleTime()
            .domain([extent(date, function(d){
                return parseDate(d)
            })])
            .range([0, width])

        const size = 50

        const lines = line()
            .x(function(d, i){
                return xScale(d.date);
            })
            .y(function(d, i){
                return yScale(d.stats);
            })

        select(node)
            .selectAll('path')
            .data(this.props.data)
            .enter()
            .append('path')

        select(node)
            .selectAll('path')
            .data(this.props.data)
            .exit()
            .remove()

        select(node)
            .selectAll('path')
            .data(this.props.data)
            .attr('fill', 'none')
            .attr('stroke', 'black')
            .attr('d', lines(this.props.data))
    }

    render() {
        return <svg ref={node => this.node = node}
        width={300} height={300}>
        </svg>
    }
}
export default LineChart
