import React, { useState, useEffect, useContext } from 'react'
import 'bootstrap/dist/css/bootstrap.min.css'
import ChampionBanner from '../components/ChampionBanner';
import RolesPerformance from '../components/RolesPerformance'
import BestChamp from '../components/BestChamp';
import axios from 'axios';
import { Store } from "../../contextStore";
import Runes from '../components/Runes';
import Items from '../components/Items';
import Spells from '../components/Spells';
import SkillsOrder from '../components/SkillsOrder';
import RateStats from '../components/RateStats';
import * as ReactBootstrap from 'react-bootstrap';
import NoData from '../components/NoData';
import { baseUrl } from '../../config/url';




const ChampionStatsV1 = (props) => {

    const [championObj, setChampion] = useState({});
    
    const [Loading, setLoading] = useState(false);

    const { state, dispatch } = useContext(Store);


    useEffect(() => {
        setLoading(true);
        const championName = props?.match?.params?.id;
        if (championName) {
            axios.get(`${baseUrl}/lol/champs/summary?champion=${championName}&region=${state?.filters?.region || 1}&fgm=${state?.filters?.fgm || 1}&duration=${state?.filters?.duration || 1}&tier=${state?.filters?.tier || 1}&role=${state?.filters?.role || 1}`)
                .then(response => {
                    setChampion(response.data);
                    setLoading(false);
                })
                .catch(error => console.log(error));
                 setChampion({});
                 setLoading(false);

        } else {
            props.history.push('/');
        }
        
    }, [props, props?.match?.params?.id, state]);

    return (
        <section className="container-fluid">
            <div className="champion-statitics">
                <div className="container" style={{position:'relative'}}>
                 {
                     !Loading && championObj?.champion?
                     <div className="row">
                     <div className="col-xl-1 col-lg-1 col-md-auto col-sm-0"></div>
                     <div className="col-xl-10 col-lg-10 col-md-12 col-sm-12">
                     <div className="mobalysis_detials">
                        <div className="mobalysis_container">
                        <div className="mobalysis_container-banner">  
                        <ChampionBanner champion={championObj?.champion} />
                        <RateStats champion={championObj}/>
                        </div>
                        <div className="mobalysis_container-roles">
                        <RolesPerformance rolePerformance={championObj?.role_performance} />
                        </div>
                        </div>
                        <div className="mobalysis_container_section-one">
                              <div className="mobalysis_container-runes">
                              <Runes champion = {championObj?.champion}  />
                              </div>
                              <div className="mobalysis_container-spells">
                              <Spells champion = {championObj?.champion}  />
                              <Items champion = {championObj?.champion}  />
                              </div> 
                              
                        </div>
                        <div className="mobalysis_container_section-two">
                            <div className="mobalysis_conatiner-skills">
                            <SkillsOrder champion = {championObj?.champion}  />
                            </div> 
                            <div className="mobalysis_conatiner-champ">
                            <BestChamp summoners={championObj?.best_players} champion={championObj?.champion} />
                            </div> 
                        </div>
                     </div>
                        
                     </div>
                     <div className="col-xl-1 col-lg-1 col-md-auto col-sm-0">
                      
                     </div>
                 </div> : (<ReactBootstrap.Spinner animation="border" className="spinner"  style={{position:'absolute',top:'1rem',left:'35rem'}}/> )
                 }
                   
                </div>
            </div>
        </section> 
    )
}

export default ChampionStatsV1