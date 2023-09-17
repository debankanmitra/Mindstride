import styled from 'styled-components'

// eslint-disable-next-line react-refresh/only-export-components
const Wrapper = styled.section`
padding: 5px;
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
  `;

function nav() {
  return (
    <>
    <Wrapper>
    <nav>       
        <li><a href="#">About</a></li>
        <li><a href="#">How it Works</a></li>
        <li><a href="#">Contact</a></li>       
    </nav>
    </Wrapper>
    </>
  )
}

export default nav;
