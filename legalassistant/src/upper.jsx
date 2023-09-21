import styled from "styled-components";
import Header from "./header";
import Landing from "./landingpage";

// eslint-disable-next-line react-refresh/only-export-components
const Wrapper = styled.section`
    width: 100%;
    height: 105vh;
    /* background: #010203ff; */
    background: radial-gradient(at bottom left,#021933,#000523,#010203ff 50%);

    @media only screen and (max-width: 767px){
        height: 140vh;

    }
`;
function upper() {
  return(
    <Wrapper>
     <Header/>
     <Landing />
    </Wrapper>
  )
}

export default upper;
