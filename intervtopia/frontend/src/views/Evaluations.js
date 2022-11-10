import React from "react";

// react-bootstrap components
import {
  Badge,
  Button,
  Card,
  Navbar,
  Nav,
  Table,
  Container,
  Row,
  Col,
  Form,
  OverlayTrigger,
  Tooltip,
} from "react-bootstrap";

import evaluation from "backend_data/evaluation_res";
import interviews_list from "backend_data/interviews_list";

function RatingImage(props){
  if(props.value == 5){
    return <img src={require("../assets/img/Ratings/rating=5.png")} className='img-fluid shadow-4' />
  }
  else if(props.value >= 4.5){
    return <img src={require("../assets/img/Ratings/rating=4.5.png")} className='img-fluid shadow-4' />
  }
  else if(props.value >= 4){
    return <img src={require("../assets/img/Ratings/rating=4.png")} className='img-fluid shadow-4' />
  }
  else if(props.value >= 3.5){
    return <img src={require("../assets/img/Ratings/rating=3.5.png")} className='img-fluid shadow-4' />
  }
  else if(props.value >= 3){
    return <img src={require("../assets/img/Ratings/rating=3.png")} className='img-fluid shadow-4' />
  }
  else if(props.value >= 2.5){
    return <img src={require("../assets/img/Ratings/rating=2.5.png")} className='img-fluid shadow-4' />
  }
  else if(props.value >= 2){
    return <img src={require("../assets/img/Ratings/rating=2.png")} className='img-fluid shadow-4' />
  }
  else if(props.value >= 1.5){
    return <img src={require("../assets/img/Ratings/rating=1.5.png")} className='img-fluid shadow-4' />
  }
  else if(props.value >= 1){
    return <img src={require("../assets/img/Ratings/rating=1.png")} className='img-fluid shadow-4' />
  }
  else if(props.value >= 0.5){
    return <img src={require("../assets/img/Ratings/rating=0.5.png")} className='img-fluid shadow-4' />
  }
  else{
    return <img src={require("../assets/img/Ratings/rating=0.png")} className='img-fluid shadow-4' />
  }

}

function Evaluations() {
  return (
    <>
      <Container fluid>
        <Row>
          <Col md="12">
            <Card>
              <Card.Header>
              <Card.Title as="h4">Your Evaluation Results</Card.Title>
              </Card.Header>
              <Card.Body >
                <Row>
                <Col md="4">
                <div className="table-full-width">
                  <Table className="table-borderless">
                    <tbody>
                    {
                      evaluation.map((element, index) => {
                        if(element.dimension !== "comment"){
                          return <tr key={index}>
                          <td className="text-left">
                              <div>
                              {element.dimension}{":"}{"  "}
                              <RatingImage value={element.value}></RatingImage>{" "}{" "}
                              {element.value}
                              </div>
                            </td>
                        </tr>;
                        }
                      })
                    }
                      </tbody>
                    </Table>
              </div>
                </Col>
                <Col md="8">
                <div className="table-full-width">
                  <Table className="table-borderless">
                    <tbody>
                    {
                      evaluation.map((element, index) => {
                        if(element.dimension === "comment"){
                          return <tr key={index}>
                          <td className="text-left">
                              <div>
                              "{element.other}"
                              </div>
                            </td>
                        </tr>;
                        }
                      })
                    }
                      </tbody>
                    </Table>
              </div>
                </Col>
                </Row>
              </Card.Body>
            </Card>
          </Col>
        </Row>
        <Row>
          <Col md="12">
            <Card>
              <Card.Header>
              <Card.Title as="h4">Evaluate a Recent Interview</Card.Title>
              </Card.Header>
              <Card.Body >
              <Table className="table-hover table-striped">
                  <thead>
                    <tr>
                      <th className="border-0">Match Name</th>
                      <th className="border-0">Interview Time</th>
                      <th className="border-0">Actions</th>
                    </tr>
                  </thead>
                  <tbody>
                  {
                    interviews_list.map((element, index) => {
                      if(element.evaluated === "No"){
                        return <tr key={index}>
                         <td>{element.name}</td>
                        <td>{element.time}</td>
                        <td>
                        <div className="text-left">
                        <Button variant="primary" className="btn-fill mr-3" size="sm">
                        Evaluate
                        </Button>
                        </div>
                        </td>
                        </tr>;
                      }
                    })
                  }
                  </tbody>
                </Table>
              </Card.Body>
            </Card>
          </Col>
        </Row>
      </Container>
    </>
  );
}

export default Evaluations;
