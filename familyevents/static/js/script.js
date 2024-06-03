function hmaction(){
    if (window.innerWidth <= 425) {
        a=document.getElementsByClassName('glass-bar');
        if(a[0].style.display==="block"){
            a[0].style.display="none";
        }
        else{
            a[0].style.display="block";
        }
    }
}
document.addEventListener("DOMContentLoaded", () => {
    const elements = document.querySelectorAll(".need-service, .black-box-one, .counters, .card, .brown-box-one, .service-card, .create-service");
  
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add("show-service");
          observer.unobserve(entry.target); 
        }
      });
    }, {
      threshold: 0.1 
    });
  
    elements.forEach(el => {
      observer.observe(el);
    });
  });
function newworks(){
    var link="{% url 'services' %}";
    window.location.href=link
}