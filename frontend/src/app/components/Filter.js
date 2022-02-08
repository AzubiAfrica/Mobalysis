import React, { useContext, useEffect, useState } from 'react';
import './Filter.css';
import { Store } from "../../contextStore";
import 'bootstrap/dist/css/bootstrap.min.css'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faSearch, faRedoAlt } from '@fortawesome/free-solid-svg-icons'
import axios from 'axios';
import ReactTooltip from 'react-tooltip'
import { Link, NavLink, useLocation } from 'react-router-dom';
import { baseUrl } from '../../config/url';


const Filter = () => {
  const [selectRegion, setSelectRegion] = useState('All Regions');
  const [selectFGM, setSelectFGM] = useState('All Modes');
  // const [selectDuration, setSelectDuration] = useState('Duration');
  const [selectTier, setSelectTier] = useState('All Tiers');
  const [selectRole, setSelectRole] = useState('All Roles');
  const [selectAllchamp, setSelectAllchamp] = useState('All Champions');
  const [champions, setChampions] = useState([]);
  const [championsAlt, setChampionsAlt] = useState([]);

  const { state, dispatch } = useContext(Store);
  const location = useLocation();

  useEffect(() => {
    axios.get(`${baseUrl}/lol/champs`)
      .then(response => {
        const sortedChampions = sortData(response.data?.champions || []);
        setChampions(sortedChampions);
        setChampionsAlt(sortedChampions);
      })
      .catch(error => {
        console.log(error);
        setChampions([]);
      });
  }, []);

  useEffect(() => {
    if (location.pathname === '/') {
      let filters = {
        region: 1,
        tier: 1,
        fgm: 1,
        duration: 1,
        champion: 'All'
      }
  
      setSelectRegion('All Regions');
      setSelectFGM('All Modes');
      setSelectTier('All Tiers');
      setSelectRole('All Roles');
      setSelectAllchamp('All Champions');
  
      dispatch({
        type: "UPDATE_FILTERS",
        payload: filters,
      });
  
    } else {
      let champId = location.pathname.split('/')[2];
      setSelectAllchamp(champId);
    }
  }, [location, dispatch]);

  const sortData = (championsData) => {
    let sortedChampions = [];
    sortedChampions = championsData.sort((a, b) => {
        let fa = a.name.toLowerCase(),
            fb = b.name.toLowerCase();
    
        if (fa < fb) {
            return -1;
        }
        if (fa > fb) {
            return 1;
        }
        return 0;
    });
    return sortedChampions;
}

  const searchChampions = (event) => {
    console.log(event.target.value);
    let filter = event.target.value.toLowerCase();
    let filteredChampions = championsAlt.filter(item => item.id.toLowerCase().includes(filter));
    setChampions(filteredChampions);
  }

  const resetFilters = () => {

    let filters = {
      region: 1,
      tier: 1,
      fgm: 1,
      duration: 1,
      champion: 'All'
    }

    setSelectRegion('All Regions');
    setSelectFGM('All Modes');
    setSelectTier('All Tiers');
    setSelectRole('All Roles');
    setSelectAllchamp('All Champions');

    dispatch({
      type: "UPDATE_FILTERS",
      payload: filters,
    });

  }

  const setfilters = (filters) => {

    dispatch({
      type: "UPDATE_FILTERS",
      payload: filters,
    });
  }
  const championStyle = {
    display: 'grid',
    gridColumnTemplate: `repeat(4,1fr)`,
    columnGap: '.4rem'
  }
  const champImg = {
    width: '35px',
    height: '35px'
  }
  return (
    <React.Fragment>
      <ul className="nav">
      <li className="nav-item">
          <a className="nav-link dropdown-toggle" style={{ fontSize: 12, color: '#fff' }}>
            {selectAllchamp}
          </a>
          <ul className="drop-menu listchamps">
            <li>
            <form>
                <input className="form-control" type="search" 
                  placeholder="Champion" aria-label="Search" onChange={searchChampions} />
                <FontAwesomeIcon icon={faSearch} className="searchicon" />
              </form>
            </li>
            <div className="listchamp">
            
              {
                champions && champions.length > 0 &&
                champions.map((champ, index) => {
                  return (
                    <NavLink to={{pathname: `/championstats/${champ?.id}`}} key={index}>
                     <li className="nav-link" key={index} onClick={()=> setSelectAllchamp(champ?.name)}>
                     
                     <img src={champ?.image} alt={champ?.id} style={champImg} /> <span>{champ?.name}</span>
                    
                     </li>
                     </NavLink>
                  )
                })
              }
            </div>
          </ul>
        </li>
        <li className="nav-item">
          <a className="nav-link dropdown-toggle" style={{ fontSize: 12, color: '#fff' }}>
            {selectRegion}
          </a>
          <ul className="drop-menu grid-section reg">
            <div className="listregion">
              <li className="nav-link" onClick={() => { setfilters({ ...state?.filters, region: 1 }); setSelectRegion('All Regions'); }}>All Regions</li>
              <li className="nav-link" onClick={() => { setfilters({ ...state?.filters, region: 2 }); setSelectRegion('BR'); }}> BR</li>
              <li className="nav-link" onClick={() => { setfilters({ ...state?.filters, region: 3 }); setSelectRegion('RU'); }}>RU</li>
              <li className="nav-link" onClick={() => { setfilters({ ...state?.filters, region: 4 }); setSelectRegion('EUW'); }}>EUW</li>
              <li className="nav-link" onClick={() => { setfilters({ ...state?.filters, region: 5 }); setSelectRegion('EUN'); }}>EUN</li>
              <li className="nav-link" onClick={() => { setfilters({ ...state?.filters, region: 6 }); setSelectRegion('LA'); }}>LA</li>
              <li className="nav-link" onClick={() => { setfilters({ ...state?.filters, region: 7 }); setSelectRegion('NA'); }}>NA</li>
              <li className="nav-link" onClick={() => { setfilters({ ...state?.filters, region: 8 }); setSelectRegion('KR'); }}>KR</li>
              <li className="nav-link" onClick={() => { setfilters({ ...state?.filters, region: 9 }); setSelectRegion('TR'); }}>TR</li>
              <li className="nav-link" onClick={() => { setfilters({ ...state?.filters, region: 10 }); setSelectRegion('JP'); }}>JP</li>
            </div>
          </ul>
        </li>
        {/* <li className="nav-item">
          <a className="nav-link dropdown-toggle" style={{ fontSize: 12, color: '#fff' }}>
            {selectFGM}
          </a>
          <ul className="drop-menu">
            <li className="nav-link" onClick={() => { setfilters({ ...state?.filters, fgm: 1 }); setSelectFGM('All Modes'); }}><span>All Modes</span></li>
            <li className="nav-link" onClick={() => { setfilters({ ...state?.filters, fgm: 2 }); setSelectFGM('ARAM'); }}><span>ARAM</span></li>
            <li className="nav-link" onClick={() => { setfilters({ ...state?.filters, fgm: 3 }); setSelectFGM('URF'); }}><span>URF</span></li>
            <li className="nav-link" onClick={() => { setfilters({ ...state?.filters, fgm: 4 }); setSelectFGM('CLASSIC'); }}><span>CLASSIC</span></li>
          </ul>
        </li> */}
        <li className="nav-item">
          <a className="nav-link dropdown-toggle" style={{ fontSize: 12, color: '#fff' }}>
            {selectTier}
          </a>
          <ul className="drop-menu">
          <div className="listregion">
            <li className="nav-link" onClick={() => { setfilters({ ...state?.filters, tier: 1 }); setSelectTier('All Tiers'); }}>All Tiers</li>
            <li className="nav-link" onClick={() => { setfilters({ ...state?.filters, tier: 2 }); setSelectTier('Challenger'); }}> Challenger</li>
            <li className="nav-link" onClick={() => { setfilters({ ...state?.filters, tier: 3 }); setSelectTier('Grandmaster'); }}>Grandmaster</li>
            <li className="nav-link" onClick={() => { setfilters({ ...state?.filters, tier: 4 }); setSelectTier('Master'); }}>Master</li>
            <li className="nav-link" onClick={() => { setfilters({ ...state?.filters, tier: 5 }); setSelectTier('Diamond'); }}>Diamond</li>
            <li className="nav-link" onClick={() => { setfilters({ ...state?.filters, tier: 6 }); setSelectTier('Platinum'); }}>Platinum</li>
            <li className="nav-link" onClick={() => { setfilters({ ...state?.filters, tier: 7 }); setSelectTier('Gold'); }}>Gold</li>
            <li className="nav-link" onClick={() => { setfilters({ ...state?.filters, tier: 8 }); setSelectTier('Silver'); }}>Silver</li>
            <li className="nav-link" onClick={() => { setfilters({ ...state?.filters, tier: 9 }); setSelectTier('Bronze'); }}>Bronze</li>
            <li className="nav-link" onClick={() => { setfilters({ ...state?.filters, tier: 10 }); setSelectTier('Iron'); }}>Iron</li>
            </div>
          </ul>
        </li>
        <li className="nav-item">
          <a className="nav-link dropdown-toggle" style={{ fontSize: 12, color: '#fff' }}>
            {selectRole}
          </a>
          <ul className="drop-menu grid-section">
            <li className="nav-link" onClick={() => { setfilters({ ...state?.filters, role: 1 }); setSelectRole('All Roles'); }}>All Roles</li>
            <li className="nav-link" onClick={() => { setfilters({ ...state?.filters, role: 2 }); setSelectRole('Top'); }}> Top</li>
            <li className="nav-link" onClick={() => { setfilters({ ...state?.filters, role: 3 }); setSelectRole('Mid'); }}>Mid</li>
            <li className="nav-link" onClick={() => { setfilters({ ...state?.filters, role: 4 }); setSelectRole('Jungler'); }}>Jungler</li>
            <li className="nav-link" onClick={() => { setfilters({ ...state?.filters, role: 5 }); setSelectRole('Support'); }}>Support</li>
            <li className="nav-link" onClick={() => { setfilters({ ...state?.filters, role: 6 }); setSelectRole('Bot'); }}>Bot</li>
          </ul>
        </li>
        <li>
          <div className="refreshIcon" data-tip data-for="refresh" onClick={resetFilters}>
            <FontAwesomeIcon icon={faRedoAlt} className="refresh" />
            <ReactTooltip id="refresh">
              <span>Reset Filters</span>
            </ReactTooltip>
          </div>
        </li>
      </ul>
    </React.Fragment>
  )
}

export default Filter
