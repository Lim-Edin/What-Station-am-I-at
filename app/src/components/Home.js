import React from 'react'


export default function() {
  return (
    <div>
      홈 화면
    </div>
  )
}

//만약 function Hello() { return (); } 하면 아래에 export default Hello;와 같다.
//함수형 컴포넌트로, (속도빠름) state나 라이프사이클 API를 전혀 사용하지 않을 때 해당 컴포넌트는
//자체 기능이 없고 props가 들어가면 뷰가 나온다는 것 명시하기 위해 사용.
//Container컴포넌트는 클래스형 컴포넌트를 사용