import styled from "styled-components";

// eslint-disable-next-line react-refresh/only-export-components
const Wrapper = styled.section`
display: flex;
    .headline{
        /* float: left; */
        border: 1px solid #0f30b4;
        h1{
            border: 1px solid #04d326;
            font-size: 5rem;
            color: aliceblue;
        }
        h4{
            border: 1px solid #00ec20;
            font-size: 2rem;
            color: antiquewhite;
        }
    }
    .dblob{
        border: 1px solid #0f30b4;
        /* padding: 20px 20px 20px 20px; */
        /* display: grid;
        place-items: center; */
        img{
            border: 1px solid #00ec20;
            width: 70%;
            float: right;
        }
    }
`;

function landingpage() {
  return (
    <>
    <Wrapper>
    <div className="headline">
    <h1>Empower Your Legal <br/>   Practice with AI <br/> Assistance</h1><br/>
    <h4>Your Trusted Partner in Legal Innovation <br/> with futuristic AI brain with legal documents</h4>
    </div>
    <div className="dblob">
    <img src="/vite.svg" alt="" />   
    </div>
    </Wrapper>
    </>
  )
}

export default landingpage;
