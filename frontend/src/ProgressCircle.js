import React, { Component } from 'react'
import './App.css'
import { axisBottom, axisLeft } from 'd3-axis'
import { select } from 'd3-selection'
import { scaleLinear, scaleTime } from 'd3-scale'
import { arc, pie } from 'd3-shape'
import { timeParse, timeFormat } from 'd3-time-format'
import { extent, max, min } from 'd3-array'

class ProgressCircle extends Component {
    constructor(props) {
        super(props)
        this.createProgressCircle = this.createProgressCircle.bind(this)
    }

    componentDidMount() {
        this.createProgressCircle()
    }

    componentDidUpdate() {
        this.createProgressCircle()
    }

    createProgressCircle() {
        const node = this.node
        var data = 45

        var margin = ({top: 20, right: 20, bottom: 30, left: 30})
        var width = this.props.size[0] - margin.left - margin.right
        var height = this.props.size[1] - margin.top - margin.bottom

        var pies = pie()
                    .sort(null)

        var calcPercent = (percent) => {
            return [percent, 100 - percent]
        }

        var dataset = {
            lower: calcPercent(0),
            upper: calcPercent(data)
        }

        var radius = min([width, height]) / 3

        const arcGenerator = arc
                            .innerRadius(radius*0.8)
                            .outerRadius(radius)
                            .startAngle(0)
                            .cornerRadius(5)

        console.log(arcGenerator)

        select(node)
            .selectAll('path')
            .data(pies(dataset.lower))
            .enter()
            .append('path')
            .attr('class', function(d,i){
                return 'color' + i
            })
            .attr('d', arcGenerator(data))
            .each(function(d){
                this._current = d;
            })
    }

    render() {
        return <svg ref={node => this.node = node}
        width={1000} height={400}>
        </svg>
    }
}
export default ProgressCircle
