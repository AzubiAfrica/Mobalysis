import React, { useEffect,  useState, useContext } from 'react'
import axios from 'axios';
import { NavLink } from 'react-router-dom';
import * as ReactBootstrap from 'react-bootstrap';
import { Store } from "../../contextStore";
import NoData from '../components/NoData';
import { baseUrl } from '../../config/url';
import PaginationComponent from '../components/Pagination';
const ChampionsV1 = () => {

    const [champions, setChampions] = useState([]);
    const [Loading,setLoading] = useState(false);
    const { state } = useContext(Store);
    const [currentPage,setCurrentPage]= useState(1);
    const [championPerPage]=useState(50);
    const [championsAlt, setChampionsAlt] = useState([]);
   


    useEffect(() => {
        
       setLoading(true);
       axios.get(`${baseUrl}/lol/champs/?champion=${state?.filters?.champion || 'All'}&region=${state?.filters?.region || 1}&tier=${state?.filters?.tier || 1}&role=${state?.filters?.role || 1}&fgm=${state?.filters?.fgm || 1}`)
            .then(response => {
                const sortedChampions = sortData(response.data?.champions || []);
                setChampions(sortedChampions);
                setChampionsAlt(sortedChampions);
                setLoading(false);
            })
            .catch(error => {
                console.log(error);
                setChampions([]);
                setLoading(false);  
            });  
           
    },[state]);

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
        return sortedChampions
    }
    // pagination codes
    const indexOfLastChampion = currentPage * championPerPage;
    const indexOfFirstChampion = indexOfLastChampion - championPerPage;
    const currentChampions = champions.slice(indexOfFirstChampion,indexOfLastChampion);
    const paginate = (pageNumber)=>setCurrentPage(pageNumber);

    // search codes
    
  const searchChampions = (event) => {
    let filter = event.target.value.toLowerCase();
    let filteredChampions = championsAlt.filter(item => item.name.toLowerCase().includes(filter));
    setChampions(filteredChampions);
  }
  const handleNextBtn = (page)=>{
      setCurrentPage(currentPage + 1);
      if(currentPage + 1 > page.length){
         setCurrentPage(1)
      }
  }
  const handlePrevBtn = ()=>{
    setCurrentPage(currentPage - 1);
    if(currentPage - 1 < 1){
        setCurrentPage(1);
     }
}

    return (
        <section>
            <div className="champions">
                       <div className="row">
                        <div className="col-xl-2 col-lg-2"></div>
                        <div className="col-xl-8 col-lg-8">
                        <div className="row">
                        <div className="col-lg-6">
                        <PaginationComponent
                           championPerPage={championPerPage} 
                           totalChampions={champions.length}
                           paginate={paginate}
                           currentPage={currentPage}
                           handleNext = {handleNextBtn}
                           handlePrev = {handlePrevBtn}
                        />
                        </div>
                        <div className="col-lg-6 d-flex flex-row-reverse">
                        <input type="search" 
                        className="form-control" 
                        placeholder="Search" 
                        style={{width:"240px",height:"40px"}} onChange={searchChampions}/>
                  
                        </div>
                        </div>

                        <div className="mobalysis_champions">

                        <div className="mobalysis_champion-container table-responsive">
                        <table className="table table-borderless table-striped table-hover table-primary">
                        <thead>
                        <tr>
                        <th>#</th>
                        <th>Champion Image</th>
                        <th>Champion Name</th>
                        <th>Champion title</th>
                        </tr>
                        </thead>
                        <tbody>
                    
                        {
                            !Loading ?
                            champions && champions.length > 0 ?
                            currentChampions.map((champion, index) => {
                                return(
                                    <tr>
                                    <td>{index+1}</td>
                                    <td>
                                    <NavLink to={{pathname: `/championstats/${champion?.id}`}} className="name-link">
                                    <img src={champion?.image} alt={champion?.id} className="champimg"/>
                                    </NavLink>
                                    </td>
                                      <td>
                                      <NavLink to={{pathname: `/championstats/${champion?.id}`}} className="name-link">
                                      <h3 className="champname">{champion?.name}</h3>
                                    </NavLink>
                                      </td>
                                      <td>
                                      <p className="champnick" style={{textTransform: "capitalize"}}>{champion?.title}</p>
                                      </td>
                                      </tr>
                                ); 
                            }) : (<div className="nodata w-50"> <NoData/> </div>)  
                            : (<ReactBootstrap.Spinner animation="border" className="spinner" /> )
                        }
                       
                      
                        </tbody>
                        </table>
                        </div>
                            </div>
                        </div>
                        <div className="col-xl-2 col-lg-2"></div>
                    </div>
               
            </div>
        </section>
    )
}

export default ChampionsV1
