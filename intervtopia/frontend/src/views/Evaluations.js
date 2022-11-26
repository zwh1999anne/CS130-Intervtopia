import React, { useState }  from "react";

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
  Modal,
  OverlayTrigger,
  Tooltip,
} from "react-bootstrap";

import evaluation from "backend_data/evaluation_res";
import interviews_list from "backend_data/interviews_list";
import { getEvalForm, evalConfirmed } from "backend_data/evaluation_form";

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

function EvaluationModal(props){
  const eval_questions = getEvalForm();
  var res_dict = {};
  return (
    <Modal
      {...props}
      size="lg"
    >
      <Modal.Header closeButton>
        <Modal.Title id="contained-modal-title-vcenter">
          Please fill in the evaluation form for {props.name}
        </Modal.Title>
      </Modal.Header>
      <Modal.Body>
      <Table>
        <tbody>
          {
          eval_questions.map((element) => {
            if(element.type === "rating"){
              res_dict[element.dimension] = 5;
              return <tr key={element.dimension}>
              <Form.Group>
              <Form.Label>Please rate the {element.dimension}</Form.Label>
              <Form.Select defaultValue={5}  className="form-control" onChange={(e) => {res_dict[element.dimension] = e.currentTarget.value;}}>
                <option value={5}>5</option>
                <option value={4}>4</option>
                <option value={3}>3</option>
                <option value={2}>2</option>
                <option value={1}>1</option>
              </Form.Select>
              </Form.Group>
              </tr>
            }
            else if(element.type === "text"){
              res_dict[element.dimension] = "";
              return <tr key={element.dimension}>
              <Form.Group className="mb-3">
              <Form.Label>(Optional) Please leave a comment for {props.name}</Form.Label>
              <Form.Control
              defaultValue=""
              placeholder="Enter your comment here."
              as="textarea" rows={3} 
              onChange={(e) => {res_dict[element.dimension] = e.currentTarget.value}}></Form.Control>
              </Form.Group>
              </tr>
            }
          } )
        }
         </tbody>
      </Table>
      </Modal.Body>
      <Modal.Footer>
      <Button variant="primary" className="btn-fill" onClick={() => {props.submitted();evalConfirmed(props.name, res_dict)}}>
           Submit
      </Button>
      <Button variant="secondary" className="btn-fill" onClick={props.onHide}>Cancel</Button>
      </Modal.Footer>
    </Modal>
  );
}

function Evaluations() {
  const [interviewlist, setinterviewList] = useState(interviews_list);

  const [evalModalShow, setevalModalShow] = React.useState(false);
  const [EvalModalName, setEvalModalName] = React.useState(" ");

  const updateEvaluationsArray = (name) => {
    setinterviewList(current =>
      current.map(obj => {
        if (obj.name === name) {
          return {...obj, evaluated:"Yes"};
        }

        return obj;
      }),
    );
  };

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
                    interviewlist.map((element) => {
                      if(element.evaluated === "No"){
                        return <tr key={element.id}>
                         <td>{element.name}</td>
                        <td>{element.time}</td>
                        <td>
                        <div className="text-left">
                        <Button variant="primary" className="btn-fill mr-3" size="sm" 
                        onClick={() => {setevalModalShow(true); setEvalModalName(element.name)}}>
                        Evaluate
                        </Button>
                        <EvaluationModal name = {EvalModalName} show={evalModalShow} onHide={() => setevalModalShow(false)}
                          submitted={() => {setevalModalShow(false); updateEvaluationsArray(EvalModalName)}}></EvaluationModal>
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
