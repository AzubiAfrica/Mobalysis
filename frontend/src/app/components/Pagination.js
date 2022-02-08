import React,{useState} from 'react'
import  Pagination  from 'react-bootstrap/Pagination'

const PaginationComponent = ({championPerPage,totalChampions,paginate,currentPage,handleNext,handlePrev}) => {
 
  const pages = Math.ceil(totalChampions/championPerPage);
   const pageNumber = [];
   for(let i=1;i<=pages;i++){
       pageNumber.push(i)
   }

    return (
        <Pagination>
          <Pagination.Prev onClick={()=>handlePrev(pageNumber)}/>
          {pageNumber.map(number=>(
            <Pagination.Item key={number} className={currentPage===number && "active"} onClick={()=>paginate(number)}>{number}</Pagination.Item>
          ))}
           
          <Pagination.Next onClick={()=>handleNext(pageNumber)}/>
        </Pagination>
    )
}

export default PaginationComponent
