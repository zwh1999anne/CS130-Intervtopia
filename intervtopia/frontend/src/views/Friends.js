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
  Form,
  Modal,
  OverlayTrigger,
  Tooltip,
} from "react-bootstrap";

import invitations from "backend_data/inivitation_list";
import friends from "backend_data/friends_list";

function SendMessageModal(props) {
  return (
    <Modal
      {...props}
      size="lg"
    >
    <Modal.Header closeButton>
        <Modal.Title id="contained-modal-title-vcenter">
        </Modal.Title>
      </Modal.Header>
      <Modal.Body>
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

function Friends() {
  const [invitationlist, setinvitationList] = useState(invitations);

  const deleteInvitation = (id) => {
    
  };

  const [sendMessageModalShow, setsendMessageModalShow] = React.useState(false);
  const [MessageModalName, setMessageModalName] = React.useState(" ");

  return (
    <>
      <Container fluid>
        <Row>
        <Col md="12">
        <Card className="strpied-tabled-with-hover">
              <Card.Header>
                <Card.Title as="h4">Pending Invitations</Card.Title>
              </Card.Header>
              <Card.Body>
              <div className="table-full-width">
                  <Table>
                    <tbody>
                    {
                      invitationlist.map((element) => {
                        return <tr key={element.id}>
                          <td className="text-left">
                              <div>
                              {element.name} has sent you a friend invitation on {element.time}!
                              </div>
                              <div className="text-secondary">
                              "{element.message}"
                              </div>
                            </td>
                            <td>
                            <Button variant="primary" className="btn-fill mr-5" size="sm">
                          Accept
                          </Button>{' '}
                          <Button variant="primary" className="mr-5" size="sm" onClick={() => deleteInvitation(element.id)}>Ignore</Button>
                            </td>
                        </tr>;
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
                <Card.Title as="h4">Friends List</Card.Title>
              </Card.Header>
              <Card.Body className="table-full-width table-responsive px-0">
                <Table className="table-hover table-striped">
                  <thead>
                    <tr>
                      <th className="border-0">Name</th>
                      <th className="border-0" width="670">Lastest Message</th>
                      <th className="border-0">Actions</th>
                    </tr>
                  </thead>
                  <tbody>
                  {
                    friends.map((element) => {
                      return <tr key={element.id}>
                         <td>{element.name}</td>
                        <td className="text-secondary">"{element.message}"</td>
                        <td>
                        <div className="text-left">
                        <Button variant="primary" className="btn-fill mr-3" size="sm" onClick={() => {setsendMessageModalShow(true); setMessageModalName(element.name)}}>
                        Send a Message
                        </Button>{'     '}
                
                        <Button variant="primary" size="sm">Launch an Interview</Button>

                        <SendMessageModal name = {MessageModalName} show={sendMessageModalShow} onHide={() => setsendMessageModalShow(false)}></SendMessageModal>
                        
                        </div>
                        </td>
                        </tr>;
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

export default Friends;
