

        const sideMenu = document.querySelector("aside");
        const menuBtn = document.querySelector("#menuBtn");
        const closeBtn = document.querySelector("#closeBtn");
        const themeToggler = document.querySelector(".theme-toggler");

        menuBtn.addEventListener('click', ()=>{
        sideMenu.style.display= 'block';
        })
        closeBtn.addEventListener('click', ()=>{
        sideMenu.style.display= 'none';
        })
        
        
    
    // <!-- wishing the users -->
          var myDate = new Date();
          var hrs = myDate.getHours();
          var greet;
          if (hrs < 12)
            greet = 'Good Morning';
          else if (hrs >= 12 && hrs <= 17)
            greet = 'Good Afternoon';
          else if (hrs >= 17 && hrs <= 24)
            greet = 'Good Evening';
          document.getElementById('greetit').innerHTML ='<b>' + greet + '</b>'; 
          
          document.getElementById("current_date").innerHTML = Date();
          