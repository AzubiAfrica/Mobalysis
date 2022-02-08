import React, { useState, useEffect, useContext } from 'react';
import Conqueror from '../../images/Conqueror.png'
import { baseUrl } from '../../config/url';

import { Store } from "../../contextStore";
import axios from 'axios';
import ReactTooltip from 'react-tooltip';

const Items = ({ champion }) => {
  const { state } = useContext(Store);
  const [items, setItems] = useState([]);

  useEffect(() => {
    axios.get(`${baseUrl}/api/itembuild?champion=${champion?.id}&region=${state?.filters?.region || 1}&tier=${state?.filters?.tier || 1}&duration=${state?.filters?.duration || 1}&role=${state?.filters?.role || 1}&fgm=${state?.filters?.fgm || 1}`)
      .then(response => {
        setItems(response.data?.data);
      })
      .catch(error => {
        console.log(error);
        setItems([]);

      });

  }, [state, champion?.id]);

  return (
    <React.Fragment>
      <div className="items-section">
        <div className="itemsheader">
          <h3>{champion?.name} ITEMS</h3>
          <div className="sep"></div>
        </div>
        <div className="ItemsContent">
          <div className="ItemsComponents">
            <div className="itemtext">
              <h3>Starter items</h3>
              {/* <span>Time target</span> */}
            </div>
            <div className="ItemIconSection">
              <div className="Itemicons">
                {
                  items?.starter_items && items?.starter_items.map((item, index) => {
                    return (
                      <span className="imgspan" key={index}><img src={item?.image} alt={item?.name} width="25" height="25" data-tip data-for={item?.name} />
                        <ReactTooltip className="tooltip-info" id={item?.name} html={true}>
                          {`<strong>${item?.name}</strong><br/><br/>`.concat(item?.longDesc)}
                        </ReactTooltip>
                      </span>
                    );
                  })
                }
              </div>
              {/* <p>@ 15 sec</p> */}
            </div>
          </div>
          <div className="ItemsComponents">
            <div className="itemtext">
              <h3>Early items</h3>
            </div>
            <div className="ItemIconSection">
              <div className="Itemicons">
                {
                  items?.early_items && items?.early_items.map((item, index) => {
                    return (
                      <span className="imgspan" key={index}><img src={item?.image} alt={item?.name} width="25" height="25" data-tip data-for={item?.name} />
                      <ReactTooltip className="tooltip-info" id={item?.name} html={true}>
                          {`<strong>${item?.name}</strong><br/><br/>`.concat(item?.longDesc)}
                      </ReactTooltip>
                      </span>
                    );
                  })
                }
              </div>
              {/* <p>@ 15 sec</p> */}
            </div>
          </div>
          <div className="ItemsComponents">
            <div className="itemtext">
              <h3>Core items</h3>
            </div>
            <div className="ItemIconSection">
              <div className="Itemicons">
                {
                  items?.core_items && items?.core_items.map((item, index) => {
                    return (
                      <span className="imgspan" key={index}><img src={item?.image} alt={item?.name} width="25" height="25" data-tip data-for={item?.name} />
                      <ReactTooltip className="tooltip-info" id={item?.name} html={true}>
                          {`<strong>${item?.name}</strong><br/><br/>`.concat(item?.longDesc)}
                      </ReactTooltip>
                      </span>
                    );
                  })
                }
              </div>
              {/* <p>@ 15 sec</p> */}
            </div>
          </div>
          <div className="ItemsComponents">
            <div className="itemtext">
              <h3>Full Build</h3>
            </div>
            <div className="ItemIconSection">
              <div className="Itemicons">
                {
                  items?.full_build && items?.full_build.map((item, index)=> {
                    return (
                      <span className="imgspan" key={index}><img src={item?.image} alt={item?.name} width="25" height="25" data-tip data-for={item?.name}/>
                      <ReactTooltip className="tooltip-info" id={item?.name} html={true}>
                          {`<strong>${item?.name}</strong><br/><br/>`.concat(item?.longDesc)}
                      </ReactTooltip>
                      </span>
                    );
                  })
                }
              </div>
            </div>
          </div>
        </div>
      </div>
    </React.Fragment>

  )
}

export default Items
