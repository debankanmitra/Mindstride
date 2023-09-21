import styled from 'styled-components'

// eslint-disable-next-line react-refresh/only-export-components
const Wrapper = styled.section`
padding: 15px;
margin-left: 1.5rem; //gap between logo and menubar
nav {
    display: flex;
    font-size: 1.5rem;

    li {
      list-style-type: none;
      padding: 0px 20px 2px 20px;
      border-radius: 5px;

      a {
        color: rgba(255, 255, 255, 1);
        text-decoration: none;
      }

      &:hover {
        background: rgba(255, 255, 255, 1);
        transition: 0.2s ease-in;

        a {
          color: rgba(1, 3, 2, 1); 
          transition: 0.2s ease-in;
        }
      }
    }
  }
@media only screen and (min-width: 768px) and (max-width: 991px){
  nav{
    font-size: 1.2rem;
  }
}
@media only screen and (max-width: 767px){
  nav{
    width: 40vw;
    /* code for nav background */
    /* border: 1px solid red; */
    position: absolute;
    top: 12vh;
    display: ${props => props.isOpen? 'block':'none'}
    /* text-align: center; */
  }
  nav li a {
    padding: 5px;
    transition: color 1s ease, padding 1s ease, background-color 1s ease;
    /* display: block; */
  }
  li a:hover{
    color: #b1d4e0;
    padding-left: 30px;
  }
}
  `;

function nav({isOpen}) {
  return (
    <>
    <Wrapper isOpen={isOpen}>
    <nav>       
        <li><a href="#">About</a></li>
        <li><a href="#">How it Works</a></li>
        <li><a href="#">Contact</a></li>       
    </nav>
    {/* <div className="humbarger">
				<div className="bar"></div>
				<div className="bar2 bar"></div>
				<div className="bar"></div>
		</div> */}
    </Wrapper>
    </>
  )
}

export default nav;
