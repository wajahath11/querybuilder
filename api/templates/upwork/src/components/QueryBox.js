import React from 'react'
import {Card,Table} from 'react-bootstrap/'
import {useState} from 'react'
import axios from 'axios';
import student_objects from './student_objects.json'
function QueryBox() {
    const [query, setQuery] = useState({
        search: "",
    })
    // const [result, setResult] = useState()

    const onChange = e => setQuery({ ...query, [e.target.name]: e.target.value });

    // const newdata= student_objects.map((data) => {
    //     return (
    //         <div key = {data.id}>
    //             <h1>{data.firstName}</h1>
    //             <h1>{data.lastName}</h1>
    //             <h1>{data.Street}</h1>
    //         </div>
    //     )
    // })

    const queryData = () => {
        axios.post('http://127.0.0.1:8000/api/qurydata/',(query)) 
        .then((res) => {
            console.log(res.data)
            // setResult(res.data)
        })
    } 
    return (
        <div className="container mt-2">
            <Card>
            <Card.Header as="h5">Query here</Card.Header>
            <Card.Body>
                <Card.Title>Please input query here..</Card.Title>
                <Card.Text>
                    <div className="form-group">
                      <textarea className="form-control" name="search" onChange={(e) => {onChange(e)}} rows="3"></textarea>
                    </div>
                </Card.Text>
                
                <button className="btn btn-primary" onClick={queryData}>Query</button>
            </Card.Body>
            </Card>
            {/* {student_objects.map((data) => {
                return (
                    <div key = {data.id}>
                        <h1>{data.firstName}</h1>
                        <h1>{data.lastName}</h1>
                        <h1>{data.Street}</h1>
                    </div>
                )
            })} */}
                {/* <Table striped bordered hover className="mt-2" style={{textTransform:"uppercase"}}>
                    <thead>
                        <tr>
                        {result && Object.entries(result[0]).map(([header, type])=>{
                            return(
                                <th>{header}</th>
                            )
                        })}
                        </tr>
                    </thead>
                    <tbody>
                    {result && result.map((body,index)=>{
                        return(
                            <tr key={body.id}>
                                <td>{index+1}</td>
                                <td>{body.branch_code}</td>
                                <td>{body.branch_name}</td>
                                <td>{body.account_number}</td>
                                <td>{body.customer_account}</td>
                                <td>{body.tran_date}</td>
                                <td>{body.tran_ref_no}</td>
                                <td>{body.acc_entry_sr_no}</td>
                                <td>{body.amount}</td>
                            </tr>
                        )
                    })}
                    </tbody>
                </Table>   */}
        </div>
    )
}

export default QueryBox
