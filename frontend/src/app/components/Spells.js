import React, { useState, useEffect, useContext } from 'react'
// import Conqueror from '../../images/Conqueror.png'
import ReactTooltip from 'react-tooltip'

import { Store } from "../../contextStore";
import axios from 'axios';
import { baseUrl } from '../../config/url';

const Spells = ({ champion }) => {

    const { state } = useContext(Store);
    const [spells, setSpells] = useState([]);


    useEffect(() => {
        axios.get(`${baseUrl}/lol/spellstats?champion=${champion?.id}&region=${state?.filters?.region || 1}&tier=${state?.filters?.tier || 1}&role=${state?.filters?.role || 1}&fgm=${state?.filters?.fgm || 1}`)
            .then(response => {
                setSpells(response.data?.data);
            })
            .catch(error => {
                console.log(error);
                setSpells([]);

            });

    }, [state, champion?.id]);

    return (
        <React.Fragment>
            <div className="spells-sections">
                <div className="spellsContent">
                    <div className="Spelltext">
                        <h3>{champion?.name} SPELLS</h3>
                        <div className="sep"></div>
                    </div>
                    {
                        spells &&
                        <>
                            <div className="spellIcons">
                                <span className="imgspan"><img src={spells[0]?.spell_1_icon} alt={spells[0]?.spell_1_name} data-tip data-for={`spells_0_1_${spells[0]?.spell_1_key}`} />
                                    <ReactTooltip className="tooltip-info" id={`spells_0_1_${spells[0]?.spell_1_key}`} html={true}>
                                        {`<strong>${spells[0]?.spell_1_name}</strong><br/><br/>`.concat(spells[0]?.spell_1_description)}
                                    </ReactTooltip>
                                </span>
                                <span  className="imgspan"><img src={spells[0]?.spell_2_icon} alt={spells[0]?.spell_2_name} data-tip data-for={`spells_0_2_${spells[0]?.spell_2_key}`} />
                                    <ReactTooltip className="tooltip-info" id={`spells_0_2_${spells[0]?.spell_2_key}`} html={true}>
                                        {`<strong>${spells[0]?.spell_2_name}</strong><br/><br/>`.concat(spells[0]?.spell_2_description)}
                                    </ReactTooltip>
                                </span>
                            </div>
                        </>

                    }

                </div>
            </div>
        </React.Fragment>
    )
}

export default Spells
