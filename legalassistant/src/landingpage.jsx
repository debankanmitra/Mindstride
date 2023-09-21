import styled from "styled-components";

// eslint-disable-next-line react-refresh/only-export-components
const Wrapper = styled.section`
#main{
border: 1px solid red;
margin: 0 auto;
width: 90%;
display: flex;
justify-content: space-between;
align-items: center;
    .headline{
        /* float: left; */
        margin-right: 20px;
        border: 1px solid #0f30b4;
        h1{
            border: 1px solid #04d326;
            font-size: 6em;
            line-height: 1em;
            text-align: left; 
            color: #ffffff;
        }
        h4{
            border: 1px solid #00ec20;
            font-size: 1.25em;
            /* margin-top: 0.5rem; */
            text-align: left;
            color: #ffffff;
        }
        button{
            width: 200px;
            padding: 15px 0;
            background: #ffffff;
            border: 1px solid #ffffff;
            color: #010203ff;
            cursor: pointer;
            overflow: hidden;
            font-size: 18px;
            margin-top: 2rem;
            border-radius:30px;
            &:hover{
                background: #e6e0e0;
                border: 1px solid #e6e0e0;
            }
        }
    }
        img{
            border: 1px solid #00ec20;
            width: 30%;
            /* float: right; */
            margin-left: 20px;
        }
    }
    @media only screen and (min-width: 768px) and (max-width: 991px){
        #main .headline h1{
            font-size: 5em;
        }
        #main img{
            width: 60%;
        }
    }
    @media only screen and (max-width: 767px){
        #main .headline h1{
            font-size: 4.4rem;
            align-items: center;
        }
        #main img{
            width: 45%;
            margin-top: 3rem;
        }
        #main{
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
        }
    }
`;

function landingpage() {
  return (
    <>
    <Wrapper className="wrapper">
    <div id="main">
        <div className="headline">
        <h1>Empower Your Legal <br/>   Practice with AI <br/> Assistance</h1><br/>
        <h4><strong>Your Trusted Partner in Legal Innovation with futuristic AI brain with legal documents Large companies are using AI to charge fees, collect debts and spam consumers. Legal.AI is a highly motivated team, that builds tools to fight back. Our tools help level the playing field, giving power to the people.</strong></h4>
        <button type="button">Lets Chat</button>
        </div>
        <img src="/vite.svg" alt="" />   
    </div>
    </Wrapper>
    </>
  )
}

export default landingpage;
