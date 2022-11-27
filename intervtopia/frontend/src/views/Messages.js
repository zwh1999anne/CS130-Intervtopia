import React, { useState } from "react";

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
  Modal,
  Form,
  OverlayTrigger,
  Tooltip,
} from "react-bootstrap";

import messages_list from "backend_data/messages_list";

function ReplyMessageModal(props) {
  return (
    <Modal
      {...props}
      size="lg"
    >
    <Modal.Header closeButton>
        <Modal.Title id="contained-modal-title-vcenter">
        Replying Message to {props.name}
        </Modal.Title>
      </Modal.Header>
      <Modal.Body>
      <p>
          You can write your message to {props.name} here.
        </p>
        <Form.Group className="mb-3">
        <Form.Control
          placeholder="Enter your message here."
          as="textarea" rows={3}></Form.Control>
        </Form.Group>
      </Modal.Body>
      <Modal.Footer>
      <Button variant="primary" className="btn-fill" onClick={props.onHide}>
            Send
          </Button>
        <Button variant="secondary" className="btn-fill" onClick={props.onHide}>Cancel</Button>
      </Modal.Footer>
    </Modal>
  );
}

function Messages() {
  const [messagelist, setmessageList] = useState(messages_list);

  const deleteMessage = (id) => {
    return setmessageList([...messagelist.filter((element) => element.id !== id)]);
  };

  const [replyMessageModalShow, setreplyMessageModalShow] = React.useState(false);
  const [MessageModalName, setMessageModalName] = React.useState(" ");

  return (
    <>
      <Container fluid>

      <Row>
        <Col md="12">
        <Card className="strpied-tabled-with-hover">
              <Card.Header>
                <Card.Title as="h4">Interview Invitations</Card.Title>
              </Card.Header>
              <Card.Body>
              <div className="table-full-width">
                  <Table>
                    <tbody>
                      {
                        messagelist.map((element) => {
                          if(element.type == "interview"){
                            return <tr key={element.id}>
                          <td className="text-left">
                              <div>
                              {element.name} invited you to have an interview on {element.time}!
                              </div>
                              <div className="text-secondary" width="670">
                              "{element.message}"
                              </div>
                            </td>
                            <td>
                            <Button variant="primary" className="btn-fill mr-5" size="sm" onClick={() => deleteMessage(element.id)}>
                          Accept
                          </Button>{' '}
                          <Button variant="primary" className="mr-5" size="sm" onClick={() => deleteMessage(element.id)}>Ignore</Button>
                            </td>
                        </tr>;
                          }
                        })
                      }
                      </tbody>
                    </Table>
              </div>
              </Card.Body>
          </Card>
        </Col>
        </Row>
        <Row>
          <Col md="12">
            <Card className="strpied-tabled-with-hover">
              <Card.Header>
                <Card.Title as="h4">Friends Messages</Card.Title>
              </Card.Header>
              <Card.Body className="table-full-width table-responsive px-0">
                <Table className="table-hover table-striped">
                  <thead>
                    <tr>
                      <th className="border-0" width="670">Message</th>
                      <th className="border-0">From</th>
                      <th className="border-0">Time Received</th>
                      <th className="border-0">Actions</th>
                    </tr>
                  </thead>
                  <tbody>
                   {
                    messagelist.map((element) => {
                      if(element.type == "message"){
                        return <tr key={element.id}>
                        <td className="text-secondary">"{element.message}"</td>
                        <td>{element.name}</td>
                        <td>{element.time}</td>
                        <td>
                        <div className="text-left">
                        <Button variant="primary" className="btn-fill mr-3" size="sm"
                        onClick={() => {setreplyMessageModalShow(true); setMessageModalName(element.name)}}>
                        Reply
                        </Button>
                        <ReplyMessageModal name={MessageModalName} show={replyMessageModalShow} onHide={() => setreplyMessageModalShow(false)}></ReplyMessageModal>
                        <Button variant="primary" size="sm" onClick={() => deleteMessage(element.id)}>Delete</Button>
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

export default Messages;
