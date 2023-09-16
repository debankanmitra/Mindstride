import styled from "styled-components";
import Nav from "./nav";

// eslint-disable-next-line react-refresh/only-export-components
const Header = styled.section`
  span{
    font-size: 1.2rem;
  }
`
function header() {
  return(
    <>
    <Header>
    <span className="logo">Legal.AI</span>
    <Nav/>
    </Header>
    </>
  ) 
}

export default header;
