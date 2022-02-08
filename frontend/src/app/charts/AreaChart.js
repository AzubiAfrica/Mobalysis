import React, { Component } from 'react'
import '../../App.css'
import { axisBottom, axisLeft } from 'd3-axis'
import { select } from 'd3-selection'
import { scaleLinear, scaleTime } from 'd3-scale'
import { brushX } from 'd3-brush'
import { area, curveLinear } from 'd3-shape'
import { timeParse, timeFormat } from 'd3-time-format'
import { timeMonth } from 'd3-time'
import { extent, max, range } from 'd3-array'

class AreaChart extends Component {
    constructor(props) {
        super(props)
        this.createAreaChart = this.createAreaChart.bind(this)
    }

    componentDidMount() {
        this.createAreaChart()
    }

    componentDidUpdate() {
        this.createAreaChart()
    }

    createAreaChart() {
        const node = this.node
        const data = this.props.data

        const margin = ({top: 20, right: 20, bottom: 20, left: 20})
        const width = this.props.size[0]
        const height = this.props.size[1]

        const parseDate = timeParse('%d%m%Y')

        const xScale = scaleTime()
            .domain(extent(this.props.data, d => parseDate(d.date)))
            .range([margin.left, width - margin.right])

        const yScale = scaleLinear()
            .domain([0, max(this.props.data, d => d.value)]).nice()
            .range([height - margin.bottom, margin.top])

        const xAxis = axisBottom(xScale)
            .ticks(timeMonth.every(1))
        const yAxis = axisLeft(yScale)
            .ticks(5)

        const xTicks = timeMonth.every(1)
        function make_x_gridlines(tick) {
            return axisBottom(xScale)
                .ticks(tick)
        }

        var yRange = range(0, max(this.props.data, d => d.value)+5, 5)
        function make_y_gridlines() {
            return axisLeft(yScale)
                .tickValues(yRange)
        }

        const areaGraph = area()
            .curve(curveLinear)
            .x(d => xScale(parseDate(d.date)))
            .y0(yScale(0))
            .y1(d => yScale(d.value))

        select(node)
            .selectAll('*')
            .remove()

        select(node)
            .append('defs')
            .append('clipPath')
            .attr('id', 'clip')
            .append('rect')
            .attr('width', width-margin.right-margin.left)
            .attr('height', height)
            .attr('x', margin.left)
            .attr('y', 0)

        const brush = brushX()
            .extent([[0,0], [width,height]])
            .on('end', updateChart)

        var tooltip = select(node)
            .append("g")
            .attr('transform', `translate(${width-3*(margin.left+margin.right)},0)`)
            .style('display', 'block')

        tooltip.append('rect')
            .attr('id', 'zoom-in')
            .attr('width', width/4)
            .attr('height', margin.top)
            .attr('fill', 'white')
            .style('opacity', 0.2);

        tooltip.append('text')
            .attr('id', 'zoom-in')
            .attr('x', margin.right)
            .attr('dy', '1em')
            .style('text-anchor', 'start')
            .attr('dominant-baseline', 'middle')
            .attr('font-size', '8')
            .text('Select area to zoom in')
            .attr('fill', 'white')

        const chartGroup = select(node)
            .append('g')
            .attr('clip-path', 'url(#clip)')
            .attr('transform', `translate(${margin.left}, 0)`)

        var id = this.props.color.substr(1, this.props.color.length)

        chartGroup
            .append('linearGradient')
            .attr('id', id)
            .attr('gradientUnits', 'userSpaceOnUse')
            .attr('x1', 0).attr('y1', 0)
            .attr('x2', 0).attr('y2', height)
            .selectAll('stop')
            .data([
                {offset: '0%', color: this.props.color, opacity: 1},
                {offset: '100%', color: 'white', opacity: 0.8}
            ])
            .enter()
            .append('stop')
            .attr('offset', function(d) { return d.offset; })
            .attr('stop-color', function(d) { return d.color; })
            .attr('stop-opacity', function(d) { return d.opacity; })

        chartGroup
            .append('path')
            .datum(this.props.data)
            .attr('class', 'myArea')
            .attr('stroke', this.props.color)
            .attr('stroke-width', '2')
            .attr('d', areaGraph)
            .style('fill', `url(${this.props.color})`)

        chartGroup
            .append('g')
            .attr('class', 'brush')
            .call(brush)

        const xGroup = select(node)
            .append('g')
            .attr('transform', `translate(${margin.left}, ${height - margin.bottom})`)
            .call(xAxis)
            .attr('class', 'axis')
            .attr('id', 'x-axis')

        select(node)
            .append('text')
            .attr('transform', `translate(${width/2}, ${height+(margin.bottom/1.5)})`)
            .style('text-anchor', 'middle')
            .attr('fill', 'white')
            .attr('dominant-baseline', 'bottom')
            .attr('font-size', '12')
            .text('Date')

        select(node)
            .append('text')
            .attr('transform', 'rotate(-90)')
            .style('text-anchor', 'middle')
            .attr('fill', 'white')
            .attr('dominant-baseline', 'middle')
            .attr('font-size', '12')
            .attr('x', 0-(height/2))
            .attr('y', 0)
            .attr('dy', '0.5em')
            .text(this.props.yValue)

        select(node)
            .append('g')
            .attr('transform', `translate(${2*margin.left}, 0)`)
            .call(yAxis)
            .attr('class', 'axis')

        chartGroup
            .append('g')
            .attr('class', 'grid')
            .attr('transform', `translate(0, ${height - margin.bottom})`)
            .call(make_x_gridlines(xTicks)
              .tickSize(-height)
              .tickFormat("")
            )

        chartGroup
            .append('g')
            .attr('class', 'grid')
            .attr('transform', `translate(${margin.left}, 0)`)
            .call(make_y_gridlines()
                .tickSize(-width)
                .tickFormat("")
            )

        let idleTimeout
        function idled() { idleTimeout = null }

        function updateChart(event) {
            const extend = event.selection

            if (!extend) {
                if (!idleTimeout) {
                    return idleTimeout = setTimeout(idled, 350)
                }

                xScale.domain([4,8])
            } else {
                xScale.domain([xScale.invert(extend[0]), xScale.invert(extend[1])])

                chartGroup
                    .select('.brush')
                    .call(brush.move, null)

                select(node)
                    .selectAll('#zoom-in')
                    .remove()
                select(node)
                    .selectAll('#zoom-out')
                    .remove()

                tooltip.append("rect")
                    .attr('id', 'zoom-out')
                    .attr("width", width/4)
                    .attr("height", margin.top)
                    .attr("fill", "white")
                    .style("opacity", 0.2);

                tooltip.append("text")
                    .attr('id', 'zoom-out')
                    .attr("x", margin.left/2)
                    .attr("dy", "1em")
                    .style("text-anchor", "start")
                    .attr("dominant-baseline", "middle")
                    .attr("font-size", "8")
                    .text('Double click to zoom out')
                    .attr('fill', 'white')

                select(node)
                    .selectAll('.grid')
                    .remove()
            }

            xGroup
                .transition()
                .duration(1000)
                .call(axisBottom(xScale).tickFormat(timeFormat('%d-%b')).ticks(3))

            chartGroup
                .select('.myArea')
                .transition()
                .duration(1000)
                .attr('d', areaGraph)

            chartGroup
                .append('g')
                .attr('class', 'grid')
                .transition()
                .duration(800)
                .attr('transform', `translate(0, ${height - margin.bottom})`)
                .call(make_x_gridlines(3)
                  .tickSize(-height)
                  .tickFormat("")
                )

            chartGroup
                .append('g')
                .attr('class', 'grid')
                .transition()
                .duration(800)
                .attr('transform', `translate(${margin.left}, 0)`)
                .call(make_y_gridlines()
                    .tickSize(-width)
                    .tickFormat("")
                )
        }

        select(node)
            .on('dblclick', function() {
                xScale.domain(extent(data, d => parseDate(d.date)))

                xGroup.transition().call(axisBottom(xScale).ticks(timeMonth.every(1)))

                chartGroup
                    .select('.myArea')
                    .transition()
                    .attr('d', areaGraph)

                select(node)
                    .selectAll('#zoom-in')
                    .remove()
                select(node)
                    .selectAll('#zoom-out')
                    .remove()

                tooltip.append('rect')
                    .attr('id', 'zoom-in')
                    .attr('width', width/4)
                    .attr('height', margin.top)
                    .attr('fill', 'white')
                    .style('opacity', 0.2)

                tooltip.append('text')
                    .attr('id', 'zoom-in')
                    .attr('x', (margin.right))
                    .attr('dy', '1em')
                    .style('text-anchor', 'start')
                    .attr('dominant-baseline', 'middle')
                    .attr('font-size', '8')
                    .text('Select area to zoom in')
                    .attr('fill', 'white')

                select(node)
                    .selectAll('.grid')
                    .remove()

                chartGroup
                    .append('g')
                    .attr('class', 'grid')
                    .transition()
                    .duration(800)
                    .attr('transform', `translate(0, ${height - margin.bottom})`)
                    .call(make_x_gridlines(xTicks)
                      .tickSize(-height)
                      .tickFormat("")
                    )

                chartGroup
                    .append('g')
                    .attr('class', 'grid')
                    .transition()
                    .duration(800)
                    .attr('transform', `translate(${margin.left}, 0)`)
                    .call(make_y_gridlines()
                        .tickSize(-width)
                        .tickFormat("")
                    )
            })
    }

    render() {
        return <svg ref={node => this.node = node}
        viewBox={`0 0 500 350`}>
        </svg>
    }
}
export default AreaChart
