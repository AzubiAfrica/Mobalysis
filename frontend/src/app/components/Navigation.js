import React, { useContext, useEffect, useState, useRef } from 'react'
import { Store } from "../../contextStore";
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.bundle.js'
// import './Navigation.css'
import { Link, NavLink } from 'react-router-dom'
import Filter from './Filter';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faAngleLeft } from '@fortawesome/free-solid-svg-icons'
import { faSearch } from '@fortawesome/free-solid-svg-icons'
import Graves from '../../images/Graves.png'
import axios from 'axios';
import { baseUrl } from '../../config/url';


const Navigation = () => {
  const [showdropdown, setShowdropdown] = useState(false);
  const [showComponents, setShowComponents] = useState(false);
  const [showMenu, setShowmenu] = useState(false);
  const [selectChampionItem, setChampionItem] = useState('Champions')
  const [champions, setChampions] = useState([]);
  const [championsAlt, setChampionsAlt] = useState([]);
  let menuRef = useRef();
  const { state, dispatch } = useContext(Store);
  const [backgroundColors,setbackgroundColor] = useState(false);

  const changeBackground = () =>{
    if(window.scrollY >=30){
      setbackgroundColor(true);
    }else{
      setbackgroundColor(false);
    }
  }

  useEffect(() => {

     axios.get(`${baseUrl}/lol/champs`)
    .then(res => {
      setChampions(res.data?.champions);
      setChampionsAlt(res.data?.champions);
    })
    .catch(error => {
      console.log(error);
      setChampions([]);
    });
   
    // document.addEventListener("mousedown", (e) => {
    //   if (!menuRef.current.contains(e.target)) {
    //     setShowdropdown(false);
    //   }
    // });
    // document.addEventListener("mousedown", (e) => {
    //   setShowComponents(false);
    //   setShowmenu(false);
    // });
    changeBackground()
    window.addEventListener("scroll",changeBackground);
  }, []);

  
  const searchChampions = (event) => {
    let filter = event.target.value.toLowerCase();
    let filteredChampions = championsAlt.filter(item => item.id.toLowerCase().includes(filter));
    setChampions(filteredChampions);
  }

  // const setChampionFilter = (selectChampion) => {

  //   const filters = {...state.filters, champion: selectChampion}

  //   dispatch({
  //     type: "UPDATE_FILTERS",
  //     payload: filters,
  //   });
  // }


  const pathName = window.location.pathname;
  let headershow = 'Champions';
  if (pathName === "/") {
    headershow = "Champions";
  }
  else if (pathName === "/runes") {
    headershow = "Runes";
  } else if (pathName === "/spells") {
    headershow = "Spells";
  }

  const ChampionShow = () => {
    setShowdropdown(!showdropdown)
    setShowComponents(false)
    setShowmenu(false)

  }
  const ComponentsShow = () => {
    setShowComponents(!showComponents)
    setShowdropdown(false)
    setShowmenu(false)
  }
  const MoreShow = () => {
    setShowmenu(!showMenu)
    setShowdropdown(false)
    setShowComponents(false)

  }

  const champImg = {
    width: '35px',
    height: '35px'
  }

  return (

      <div className="Navigation-sect">
        <div className="row">
          <div className="col-xl-1 col-lg-1"></div>
          <div className="col-xl-10 col-lg-10">
            <div className={backgroundColors?'filter-section active':'filter-section'}>
                <div className="back-section">
                  <ol className="breadcrumb">
                    <li className="breadcrumb-item"><Link to="/" style={{color: "white"}}>
                       Champions
                    </Link></li>
                    {/* <li className="breadcrumb-item active" aria-current="page">{headershow}</li> */}
                  </ol>
                </div>
                <div className="search-section">
                  <Filter />
                </div>
              </div>
              {
            // <div className="nav-section">
            
              // <div className={backgroundColors ? `nav-table active`:'nav-table'}>
              //   <table className="table table-responsive" cellPadding="5" cellSpacing="5">
              //     <tr>
              //       <td>
              //         <div ref={menuRef} className={showdropdown ? `dropdown show` : 'dropdown'}>
              //           <span className="btn btn-secondary dropdown-toggle" role="button" id="champions" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" onClick={ChampionShow}>
              //             {selectChampionItem}
              //           </span>
              //           <div className={showdropdown ? `dropdown-menu champ show ` : 'dropdown-menu champ'} aria-labelledby="dropdownMenu2">
              //             <div>
              //               <form>
              //                 <input className="form-control" type="search" 
              //                   placeholder="Champion" aria-label="Search" onChange={searchChampions} />
              //                 <FontAwesomeIcon icon={faSearch} className="searchicon" />
              //               </form>
              //             </div>
              //             <div className="chamFilter">
              //               <NavLink
              //                 to={{
              //                   pathname: `/`,
              //                 }} className="name-link"
              //                 >
              //                 <div className="dropdown-item"><span>All Champions</span></div>
              //               </NavLink>
              //               {
              //                 champions && champions.length > 0 &&
              //                 champions.map((champ, index) => {
              //                   return (
              //                     <NavLink
              //                       to={{
              //                         pathname: `/championstats/${champ?.id}`,
              //                       }} className="name-link" key={index}>
              //                       <div className="dropdown-item" key={index}>
              //                         <img src={champ?.image} alt={champ?.id} style={champImg} /> <span>{champ?.name}</span>
              //                       </div>
              //                     </NavLink>

              //                   )
              //                 })
              //               }

              //             </div>
              //           </div>
              //         </div>
              //       </td>
              //       <td>
              //         <div className={showComponents ? `dropdown show` : 'dropdown'}>
              //           <span className="btn btn-secondary dropdown-toggle" role="button" id="components"
              //             data-toggle="dropdown" aria-haspopup="true"
              //             aria-expanded="false" onClick={ComponentsShow}>
              //             Components
              //           </span>

              //           <div className={showComponents ? `dropdown-menu show` : 'dropdown-menu'} aria-labelledby="components">
              //             <a className="dropdown-item" href="#">Combo showcase</a>
              //             <a className="dropdown-item" href="#">Live Guide</a>
              //             <a className="dropdown-item" href="#">Friends-widget</a>
              //             <a className="dropdown-item" href="#">Counter-helper</a>
              //           </div>
              //         </div>
              //       </td>
              //       <td>
              //         <div className={showMenu ? `dropdown show` : 'dropdown'}>
              //           <span className="btn btn-secondary dropdown-toggle"
              //             role="button" id="more" data-toggle="dropdown"
              //             aria-haspopup="true" aria-expanded="false" onClick={MoreShow}>
              //             More
              //           </span>

              //           <div className={showMenu ? `dropdown-menu show` : 'dropdown-menu'} aria-labelledby="more">
              //             <a className="dropdown-item" href="#">Early-Game suggestion</a>
              //             <a className="dropdown-item" href="#">Early-Game Articles</a>
              //             <a className="dropdown-item" href="#">Early-Game Updates</a>
              //           </div>
              //         </div>

              //       </td>

              //       {/* <td>
              //         <div className="lastupdate">
              //         <button type="button" className="btn btn-dark">
              //           <span>Last updated: 1 day ago</span>
              //         </button>
              //         </div>
              //       </td> */}
              //     </tr>
              //   </table>
              // </div>
           
            // </div>
          }
          </div>
          <div className="col-xl-1 col-lg-1"></div>
        </div>
      </div>

  )
}

export default Navigation
