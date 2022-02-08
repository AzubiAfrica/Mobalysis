import React, { useState, useEffect, useContext } from 'react'
import ReactTooltip from 'react-tooltip'
// import Top from '../../images/StatModsAttackSpeedIcon.png'
// import Precision from '../../images/7201_Precision.png'
// import Resolve from '../../images/7204_Resolve.png'
// import Conqueror from '../../images/Conqueror.png'

import { Store } from "../../contextStore";
import axios from 'axios';
import { baseUrl } from '../../config/url';

const Runes = ({ champion }) => {
  const { state } = useContext(Store);
  const [runes, setRunes] = useState([]);

  useEffect(() => {
    axios.get(`${baseUrl}/lol/runes/performance?champion=${champion?.id}&region=${state?.filters?.region || 1}&tier=${state?.filters?.tier || 1}&role=${state?.filters?.role || 1}&fgm=${state?.filters?.fgm || 1}`)
      .then(response => {
        setRunes(response.data?.runes);
      })
      .catch(error => {
        console.log(error);
        setRunes([]);

      });

  }, [state, champion?.id]);

  return (
    <React.Fragment>
      <div className="container mt-4">
        <div className="RunesSection">

          <div className="runestext">
            <h3>{champion?.name} RUNES</h3>
            <div className="sep"></div>
          </div>
          <div className="RunesContent">
            <div className="RunesComponents">
              <div className="RunesIcons">
                <div className="RunesIconText">
                  <img src={runes[0]?.primaryStyle?.icon} alt={runes[0]?.primaryStyle?.name} />
                  <div className="pre">{runes[0]?.primaryStyle?.name}</div>
                </div>
              </div>
              <div className="RunesImg">
                <div className="RunesImgList">
                  {
                    runes[0]?.primaryStyle?.keystones.map((keystone, index) => {
                      return (
                        <div className={`${!keystone?.selected ?"Runesicon active":"Runesicon"}`} data-tip data-for={keystone?.key} key={index}>
                        <img src={keystone?.icon} alt={keystone?.name} className={`${!keystone?.selected && 'selected'}`}/>
                        <ReactTooltip className="tooltip-info" id={keystone?.key} effect="solid" html={true}>
                          {`<strong>${keystone?.name}</strong><br/><br/>`.concat(keystone?.longDesc)}
                        </ReactTooltip>
                      </div>
                      )
                    })
                  }
                </div>
                <div className="RunesImgList">
                {
                    runes[0]?.primaryStyle?.slot_1.map((slot, index) => {
                      return (
                        <div  className={`${!slot?.selected ?"Runesicon active":"Runesicon"}`} data-tip data-for={slot?.key} key={index}>
                          <img src={slot?.icon} alt={slot?.name} width="25" height="25" className={`Runesicon ${!slot?.selected && 'selected'}`}/>
                          <ReactTooltip className="tooltip-info" id={slot?.key} effect="solid" html={true}>
                            {`<strong>${slot?.name}</strong><br/><br/>`.concat(slot?.longDesc)}
                          </ReactTooltip>
                        </div>
                      )
                    })
                  }
                </div>
                <div className="RunesImgList">
                {
                    runes[0]?.primaryStyle?.slot_2.map((slot, index) => {
                      return (
                        <div className={`${!slot?.selected ?"Runesicon active":"Runesicon"}`}  data-tip data-for={slot?.key} key={index}>
                        <img src={slot?.icon} alt={slot?.name} width="25" height="25" className={`Runesicon ${!slot?.selected && 'selected'}`}/>
                        <ReactTooltip className="tooltip-info" id={slot?.key} effect="solid" html={true}>
                          {`<strong>${slot?.name}</strong><br/><br/>`.concat(slot?.longDesc)}
                        </ReactTooltip>
                      </div>
                      )
                    })
                  }
                </div>
                <div className="RunesImgList">
                {
                    runes[0]?.primaryStyle?.slot_3.map((slot, index) => {
                      return (
                        <div className={`${!slot?.selected ?"Runesicon active":"Runesicon"}`}  data-tip data-for={slot?.key} key={index}>
                          <img src={slot?.icon} alt={slot?.name} width="25" height="25" className={`Runesicon ${!slot?.selected && 'selected'}`}/>
                          <ReactTooltip className="tooltip-info" id={slot?.key} effect="solid" html={true}>
                            {`<strong>${slot?.name}</strong><br/><br/>`.concat(slot?.longDesc)}
                          </ReactTooltip>
                        </div>
                      )
                    })
                  }
                </div>
              </div>
            </div>
            <div className="RunesComponents">
              <div className="RunesIcons">
                <div className="RunesIconText">
                  <img src={runes[0]?.subStyle?.icon} alt={runes[0]?.subStyle?.name} />
                  <div className="pre">{runes[0]?.subStyle?.name}</div>
                </div>
              </div>
              <div className="RunesImg">
                <div className="RunesImgList">
                {
                    runes[0]?.subStyle?.keystones.map((keystone, index) => {
                      return (
                        <div className={`${!keystone?.selected ?"Runesicon active":"Runesicon"}`} data-tip data-for={keystone?.key} key={index}>
                          <img src={keystone?.icon} alt={keystone?.name} className={`${!keystone?.selected && 'selected'}`}/>
                          <ReactTooltip className="tooltip-info" id={keystone?.key} effect="solid" html={true}>
                              {`<strong>${keystone?.name}</strong><br/><br/>`.concat(keystone?.longDesc)}
                            </ReactTooltip>
                        </div>
                      )
                    })
                  }
                </div>
                <div className="RunesImgList">
                {
                    runes[0]?.subStyle?.slot_1.map((slot, index) => {
                      return (
                        <div className={`${!slot?.selected ?"Runesicon active":"Runesicon"}`} data-tip data-for={slot?.key} key={index}>
                          <img src={slot?.icon} alt={slot?.name} width="25" height="25" className={`Runesicon ${!slot?.selected && 'selected'}`}/>
                          <ReactTooltip className="tooltip-info" id={slot?.key} effect="solid" html={true}>
                            {`<strong>${slot?.name}</strong><br/><br/>`.concat(slot?.longDesc)}
                          </ReactTooltip>
                        </div>
                      )
                    })
                  }
                </div>
                <div className="RunesImgList">
                {
                    runes[0]?.subStyle?.slot_2.map((slot, index) => {
                      return (
                        <div className={`${!slot?.selected ?"Runesicon active":"Runesicon"}`}  data-tip data-for={slot?.key} key={index}>
                          <img src={slot?.icon} alt={slot?.name} width="25" height="25" className={`Runesicon ${!slot?.selected && 'selected'}`}/>
                          <ReactTooltip className="tooltip-info" id={slot?.key} effect="solid" html={true}>
                            {`<strong>${slot?.name}</strong><br/><br/>`.concat(slot?.longDesc)}
                          </ReactTooltip>
                        </div>
                      )
                    })
                  }
                </div>
                <div className="RunesImgList">
                {
                    runes[0]?.subStyle?.slot_3.map((slot, index) => {
                      return (
                        <div className={`${!slot?.selected ?"Runesicon active":"Runesicon"}`}  data-tip data-for={slot?.key} key={index}>
                          <img src={slot?.icon} alt={slot?.name} width="25" height="25" className={`Runesicon ${!slot?.selected && 'selected'}`}/>
                          <ReactTooltip className="tooltip-info" id={slot?.key} effect="solid" html={true}>
                            {`<strong>${slot?.name}</strong><br/><br/>`.concat(slot?.longDesc)}
                          </ReactTooltip>
                        </div>
                      )
                    })
                  }
                </div>
              </div>
              <div className="RunesShards">
                <div className="RunesIcons">
                  <div className="RunesIconText">
                    <div className="pre">Shards</div>
                  </div>
                </div>
                <div className="ShardSec">
                  {
                    runes[0]?.shards?.defense.map((shard, index) => {
                      return (
                        <div className={`${!shard?.selected ?"Runesicon active":"Runesicon"}`} data-tip data-for={shard?.id} key={index}>
                          <img src={shard?.icon} alt={shard?.name} width="25" height="25" className={`${!shard?.selected && 'selected'}`} />
                          <ReactTooltip  className="tooltip-info" id={shard?.id} effect="solid" html={true}>
                            {shard?.name}
                          </ReactTooltip>
                        </div>
                      )
                    })
                  }
                </div>
                <div className="ShardSec">
                {
                    runes[0]?.shards?.flex.map((shard, index) => {
                      return (
                        <div className={`${!shard?.selected ?"Runesicon active":"Runesicon"}`} data-tip data-for={shard?.id} key={index}>
                          <img src={shard?.icon} alt={shard?.name} width="25" height="25" className={`${!shard?.selected && 'selected'}`} />
                          <ReactTooltip  className="tooltip-info" id={shard?.id} effect="solid" html={true}>
                            {shard?.name}
                          </ReactTooltip>
                        </div>
                      )
                    })
                  }
                </div>
                <div className="ShardSec">
                {
                    runes[0]?.shards?.offense.map((shard, index) => {
                      return (
                        <div className={`${!shard?.selected ?"Runesicon active":"Runesicon"}`} data-tip data-for={shard?.id} key={index}>
                          <img src={shard?.icon} alt={shard?.name} width="25" height="25" className={`${!shard?.selected && 'selected'}`} />
                          <ReactTooltip  className="tooltip-info" id={shard?.id} effect="solid" html={true}>
                            {shard?.name}
                          </ReactTooltip>
                        </div>
                      )
                    })
                  }
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </React.Fragment>
  )
}

export default Runes
