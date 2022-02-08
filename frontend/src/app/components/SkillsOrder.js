import React, { useState, useEffect, useContext } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faArrowRight } from '@fortawesome/free-solid-svg-icons'
import 'bootstrap/dist/css/bootstrap.min.css'
import NoData from './NoData'


import ReactTooltip from 'react-tooltip'

import { Store } from "../../contextStore";
import axios from 'axios';
import { baseUrl } from '../../config/url';
const SkillsOrder = ({ champion }) => {
    const { state } = useContext(Store);
    const [skills, setSkills] = useState([]);

    useEffect(() => {
        axios.get(`${baseUrl}/api/skillorder?champion=${champion?.id}&region=${state?.filters?.region || 1}&tier=${state?.filters?.tier || 1}&role=${state?.filters?.role || 1}&fgm=${state?.filters?.fgm || 1}`)
            .then(response => {
                setSkills(response.data?.data[0]);
            })
            .catch(error => {
                console.log(error);
                setSkills([]);

            });

    }, [state, champion?.id]);

    return (
        <React.Fragment>
            <div className="skill-section">
                <div className="skillHeader">
                    <h3>{champion?.name} Skill Order</h3>
                    <div className="skillalpha">
                        <div className="alpha mt-2">
                            <p style={{ color: '#FFC306' }}>W <FontAwesomeIcon icon={faArrowRight} style={{ color: '#8890B5' }} /></p>

                            <p style={{ color: '#47CC42' }}>E <FontAwesomeIcon icon={faArrowRight} style={{ color: '#8890B5' }} /></p>

                            <p style={{ color: '#38C6F4' }}>Q</p>
                        </div>
                    </div>
                </div>
                <div className="Skill-Components">
                    <div className="tableResponsive table-responsive">
                        <table className="table table-borderless">
                            <tbody>
                                <tr className="theader">
                                    <th></th>
                                    <th>1</th>
                                    <th>2</th>
                                    <th>3</th>
                                    <th>4</th>
                                    <th>5</th>
                                    <th>6</th>
                                    <th>7</th>
                                    <th>8</th>
                                    <th>9</th>
                                    <th>10</th>
                                    <th>11</th>
                                    <th>12</th>
                                    <th>13</th>
                                    <th>14</th>
                                    <th>15</th>
                                    <th>16</th>
                                    <th>17</th>
                                    <th>18</th>
                                </tr>
                                {   skills ?
                                    <>
                                    <tr>
                                    <td className="skillOrderCell">
                                        <div className="img_align_block">
                                            <div className="imgspan">
                                                <img src={skills[0]?.image} alt={skills[0]?.id} width="30" height="30" 
                                                data-tip data-for={`skills_0_${skills[0]?.id}`} />
                                                <ReactTooltip className="tooltip-info" id={`skills_0_${skills[0]?.id}`} html={true}>
                                                    {`<strong>${skills[0]?.name}</strong><br/><br/>`.concat(skills[0]?.description)}
                                                </ReactTooltip>
                                            </div>
                                        </div>
                                    </td>
                                    {
                                        [ ...Array(18) ].map((skill, index)=>{
                                            return (
                                                skills[0]?.levels.includes(parseFloat(index+1).toFixed(1).toString()) ?
                                                    <td className="skillCell active"><div className="skilltexts">Q</div></td>
                                                :
                                                    <td className="skillCell"></td>
                                            )
                                        })
                                    }
                                </tr>
                                <tr>
                                    <td className="skillOrderCell">
                                        <div className="img_align_block">
                                            <div className="imgspan">
                                                <img src={skills[1]?.image} alt={skills[1]?.id} width="30" height="30"
                                                 data-tip data-for={`skills_1_${skills[1]?.id}`} />
                                                <ReactTooltip className="tooltip-info" id={`skills_1_${skills[1]?.id}`} html={true}>
                                                    {`<strong>${skills[1]?.name}</strong><br/><br/>`.concat(skills[1]?.description)}
                                                </ReactTooltip>
                                            </div>
                                        </div>
                                    </td>
                                    {
                                        [ ...Array(18) ].map((skill, index)=>{
                                            return (
                                                skills[1]?.levels.includes(parseFloat(index+1).toFixed(1).toString()) ?
                                                    <td className="skillCellw active"><div className="skilltexts">W</div></td>
                                                :
                                                    <td className="skillCellw"></td>
                                            )
                                        })
                                    }
                                </tr>
                                <tr>
                                    <td className="skillOrderCell">
                                        <div className="img_align_block">
                                            <div className="imgspan">
                                                <img src={skills[2]?.image} alt={skills[2]?.id} width="30" height="30" 
                                                 data-tip data-for={`skills_2_${skills[2]?.id}`} />
                                                 <ReactTooltip className="tooltip-info" id={`skills_2_${skills[2]?.id}`} html={true}>
                                                    {`<strong>${skills[2]?.name}</strong><br/><br/>`.concat(skills[2]?.description)}
                                                 </ReactTooltip>
                                            </div>
                                        </div>
                                    </td>
                                    {
                                        [ ...Array(18) ].map((skill, index)=>{
                                            return (
                                                skills[2]?.levels.includes(parseFloat(index+1).toFixed(1).toString()) ?
                                                    <td className="skillCelle active"><div className="skilltexts">E</div></td>
                                                :
                                                    <td className="skillCelle"></td>
                                            )
                                        })
                                    }
                                </tr>
                                <tr>
                                    <td className="skillOrderCell">
                                        <div className="img_align_block">
                                            <div className="imgspan">
                                                <img src={skills[3]?.image} alt={skills[3]?.id} width="30" height="30" 
                                                 data-tip data-for={`skills_3_${skills[3]?.id}`} />
                                                <ReactTooltip className="tooltip-info" id={`skills_3_${skills[3]?.id}`} html={true}>
                                                    {`<strong>${skills[3]?.name}</strong><br/><br/>`.concat(skills[3]?.description)}
                                                </ReactTooltip>
                                            </div>
                                        </div>
                                    </td>
                                    {
                                        [ ...Array(18) ].map((skill, index)=>{
                                            return (
                                                skills[3]?.levels.includes(parseFloat(index+1).toFixed(1).toString()) ?
                                                    <td className="skillCellr active"><div className="skilltexts">R</div></td>
                                                :
                                                    <td className="skillCellr"></td>
                                            )
                                        })
                                    }
                                </tr>
                                </> :
                                <>
                                    <tr></tr>
                                    <tr> <NoData /></tr>
                                </>
                               
                                }
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </React.Fragment>
    )
}

export default SkillsOrder
