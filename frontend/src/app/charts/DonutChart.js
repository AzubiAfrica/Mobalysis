import React, { Component } from 'react'
import '../../App.css'
import { select } from 'd3-selection'
import { scaleOrdinal } from 'd3-scale'
import { pie, arc } from 'd3-shape'
import { entries } from 'd3-collection'
import { transition } from 'd3-transition'
import { interpolate } from 'd3-interpolate'
import { format } from 'd3-format'

class DonutChart extends Component {
    constructor(props) {
        super(props)
        this.createDonutChart = this.createDonutChart.bind(this)
    }

    componentDidMount() {
        this.createDonutChart()
    }

    componentDidUpdate() {
        this.createDonutChart()
    }

    createDonutChart() {
        const node = this.node

        var margin = this.props.margin
        var width = this.props.size[0] - margin.left - margin.right
        var height = this.props.size[1] - margin.top - margin.bottom

        var radius = width / 5

        var data = {a:this.props.data, b:100-this.props.data}

        var color = scaleOrdinal()
                    .range([this.props.color, '#70758c'])

        var opacity = scaleOrdinal()
                    .range(['1', '0.2'])

        const transitioner = transition().duration(1000)
        const formating = format('.0f')

        var pieChart = pie()
                .sort(null)
                .value(d => d.value)

        var arcGenerator = arc()
                    .innerRadius(radius)
                    .outerRadius(radius*1.3)
                    .startAngle(0)
                    .cornerRadius(10)

        var data_ready = pieChart(entries(data))

        select(node)
            .selectAll('*')
            .remove()

        select(node)
            .selectAll()
            .data(data_ready)
            .enter()
            .append('path')
            .attr('transform', `translate(${2*(margin.left+margin.right)}, ${1.8*(margin.top+margin.bottom)})`)
            .attr('d', arcGenerator)
            .style('fill', function(d){ return(color(d.data.key)); })
            .style('opacity', function(d) { return(opacity(d.data.key)); })
            .attr("stroke", "none")
            .style("stroke-width", "5px")
            .transition(transitioner)
            .attrTween('d', d => {
                let i = interpolate(d.startAngle, d.endAngle);

                return t => {
                    d.endAngle = i(t)

                    return arcGenerator(d);
                };
            })

        select(node)
            .append('text')
            .attr('transform', `translate(${2*(margin.left+margin.right)}, ${1.8*(margin.top+margin.bottom)})`)
            .transition(transitioner)
            .text(this.props.data+'%')
            .attr("font-size", "15")
            .attr('stroke', '#000')
            .attr('fill', 'white')
            .attr("text-anchor", "middle")
            .attr("dominant-baseline", "middle")
            .textTween(function(d) {
                var val = 0;
                let i = interpolate(val, data.a);

                return function(t) { return formating(val = Math.ceil(i(t)))+'%'; }
            })

        if (this.props.name == undefined) {

        } else {
            select(node)
                .append('text')
                .attr('transform', `translate(${2*(margin.left+margin.right)}, ${height-1.5*(margin.bottom+margin.top)})`)
                .text(this.props.name)
                .attr("font-size", "12")
                .attr('stroke', '#000')
                .attr('fill', 'white')
                .attr("text-anchor", "middle")
                .attr("dominant-baseline", "middle")
        }

    }

    render() {
        return <svg ref={node => this.node = node}
        viewBox={`0 0 ${this.props.svg[0]} ${this.props.svg[1]}`}>
        </svg>
    }
}
export default DonutChart
