

const badgesEl = document.querySelector('header .badges');
const toTopEl = document.querySelector('#to-top');




// window -> 프로젝트 화면! window에서 scroll하면 함수를 실행하는데 그 함수를 최대한 적게 실행하기 위해서
// throttle라는 lodash에서 제공하는 기능 도입! 
// scroll>500이면 헤더에 있는 badge를 숨기게 처리함!(display:none) -> 숨겨질 때 우측하단에 to-top버튼 나타나야함!
 


window.addEventListener('scroll', _.throttle(function(){
    console.log(window.scrollY);
    if (window.scrollY > 500) {
        //배지 숨기기 gsap.to(요소,지속시간,옵션);
        gsap.to(badgesEl, .6, {
            opacity:0,
            display : 'none'
        });
        //버튼 보이기
        gsap.to( toTopEl,.2, {
            x: 100

        });

    } else {
        //배지 보이기
        gsap.to(badgesEl, .6, {
            opacity:1,
            display : 'block'
        });
        //버튼 숨기기
        gsap.to(toTopEl,.2 ,{
            x: 100 //우측으로 사라짐 

        }); //to()안에 애니메이션을 제어하고자 하는 요소를 명시
    } 
}, 300));
//_.throttle(함수,시간)

toTopEl.addEventListener('click', function() {
    gsap.to(window, .7 ,{
        scrollTo: 0 //화면의 위치는 .7초동안 0px 지점으로 옮겨주겠다!
    })
})


//#to-top에 addEventListdner메소드(click,익명의함수) -> to-top이라는 elment를 클릭하면 익명의 함수를 실행하겠따. 
//익명의 함수는 이벤트의 핸들러라고 부른다!


const fadeEls = document.querySelectorAll('.visual .fade-in');
fadeEls.forEach(function (fadeEl, index) {
    gsap.to(fadeEl, 1, {
        delay: (index+1) * .7, //0.7, 1.4, 2.1. 2.8
        opacity: 1,
    });
});


//Swiper 자바스크립트 라이브러리를 통해서 손쉽게 요소에 슬라이드를 적용할 수 있음

new Swiper('.notice-line .swiper-container', {
    direction: 'vertical',
    autoplay: true,
    loops: true
});


new Swiper('.promotion .swiper-container', {
    slidesPerView:3, //한번에 보여줄 슬라이드 개수
    spaceBetween:10,
    centeredSlides: true,
    loop: true,
    autoplay: {
        delay: 2000
    },
    pagination: {
        el: '.promotion .swiper-pagination', //페이지 번호 요소 선택자
        clickable: true //사용자의 페이지 번호 요소 제어
    },
    navigation: {
        prevEl:'.promotion .swiper-prev',
        nextEl:'.promotion .swiper-next'
    }
});
new Swiper('.awards .swiper-container',{
    autoplay:true,
    loop:true,
    spaceBetween: 30,
    slidesPerView: 5,
    navigation: {
        prevEl:'.awards .swiper-prev',
        nextEl:'.awards .swiper-next'

    }
});

const promotionEl = document.querySelector('.promotion');
const promotionToggleBtn = document.querySelector('.toggle-promotion');
let isHidePromotion = false;
promotionToggleBtn.addEventListener('click', function () {
    isHidePromotion = !isHidePromotion
    if (isHidePromotion) {
        //숨김 처리
        promotionEl.classList.add('hide');

    } else {
        //보임 처리
        promotionEl.classList.remove('hide');

    }
});

function random(min, max) {
    // `.toFixed()`를 통해 반환된 문자 데이터를,
    // `parseFloat()`을 통해 소수점을 가지는 숫자 데이터로 변환
    return parseFloat((Math.random() * (max - min) + min).toFixed(2))
  }

function floatingObject(selector, delay, size) {
    gsap.to(selector, random(1.5,2.5), {
        y: size,
        repeat: -1,
        yoyo: true,
        ease: Power1.easeInOut,
        delay:random(0,delay)
       });

}
floatingObject('.floating1',1,15);
floatingObject('.floating2',.5,15);
floatingObject('.floating3',1.5,20);

const spyEls = document.querySelectorAll('section.scroll-spy');
spyEls.forEach(function (spyEl) {
    //Scene은 메소드임! -> ScrollMagic이라는 자바스크립트 라이브러리를 통해서
    //특정한 요소를 감시하는 옵션을 지정해주는 메소드
    //클래스 속성을 지정해서 넣었다 뺏다 제어해주는 역할
    //addTo ->ScrollMagic이라는 자바스크립트 라이브러리가 필요한 컨트롤러라는 개념을 사용하기 위해서 메소드를 추가함
    new ScrollMagic //new라는 키워드를 사용해서 ScrollMagic 자바스크립트 라이브러리를 실행하려고 함.
        .Scene( {
            triggerElement: spyEl, //객체데이터, 특정한 요소를 감시! 보여짐 여부를 감시할 요소를 지정
            triggerHook: .8
        })
        .setClassToggle(spyEl, 'show') //show라는 클래스가 사라졌다 생겼다 함!
        .addTo(new ScrollMagic.Controller()); 

})

//감시하려고 하는 section scroll-spy 클래스 속성들을 spyEls에 변수에 할당
//반복적으로 처리!! 반복될 때마다 spyEl 매개변수에 값이 들어가 있음.
//spyEl는 내가 감시하고 있는 요소임.
//triggerHook옵션은 뷰포트의 .8부터 시작!! 화면에 보여진다고 판단되면 setClassToggle 메소드 실행!
//setClassToggle(Toggle할 요소, Toggle할 클래스 이름)은 spyEl에 show를 넣었다 뺐다!
//addTo(new 자바스크립트 라이브러리.Controller(메소드)) -> ScrollMagic에서 기본적으로 추가한 옵션들을
//내부의 컨트롤러에 내용을 할당해서 실제로 동작할 수 있는 구조로 만들어줌!!
//ScrollMagic이 내부적으로 어떻게 동작하는지 알지 못하면 사용하기 난해할 수 있지만 내부에 있는 logic을 다 이해할 
//필요는 없다! 라이브러리 문서에서 제공하는 시키는대로 진행하면 됨!





//gsap 라이브러리는 기본적인 애니메이션을 충분히 많이 제공하지만 라이브러리 자체의 용량이 커져서 로드되는 시간이 오래걸림
//일부기능분리!