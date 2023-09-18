import styled from "styled-components";
import Header from "./header";

// eslint-disable-next-line react-refresh/only-export-components
const Wrapper = styled.section`
    width: 100%;
    height: 110vh;
    /* background: #010203ff; */
    background: radial-gradient(at bottom left,#021933,#000523,#010203ff 50%);
`;
function upper() {
  return(
    <Wrapper>
     <Header/>
    </Wrapper>
  )
}

export default upper;
