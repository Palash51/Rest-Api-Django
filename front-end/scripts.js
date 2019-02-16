const app = document.getElementById('root');

const logo = document.createElement('img');


const container = document.createElement('div');
container.setAttribute('class', 'container');

app.appendChild(logo);
app.appendChild(container);


// var request = new XMLHttpRequest();
// request.open('GET', 'https://1a274ad0.ngrok.io/contries/v1/', true);
// request.onload = function () {



$(document).ready(function(){

  $.ajax({
        method: "GET",
        url: 'https://f12c6680.ngrok.io/contries/v1/',
        // headers: {
        //     "Authorization": 'Token ' + localStorage.getItem('Token')
        // },
        contentType: 'application/json',
        // async: false,
        success: function (data) {
            // console.log(data)
            cdata = data.data;
            // console.log(cdata)
            var countryName=document.getElementById('country')
            for(i=0;i<cdata.length;i++){

              // console.log(cdata[i].name);
              var url="";
              $('#country').append("<li class='country_name' name="+cdata[i].name+">"+cdata[i].name+"</li>");
            

          }

            $('ul li.country_name').click(function (e) {
            e.preventDefault();
            console.log(e.target.innerText);

            var country_name = e.target.innerText;
            var data = {
                country_name: country_name,
            }

            $.ajax({

              method: "POST",
              url : "https://f12c6680.ngrok.io/country/name/v1/",
              contentType: 'application/json',   
              data: JSON.stringify(data),
              success: function (data) {
                  // document.location.reload();
                  console.log(data.data);
                  window.location = "country_details.html"

              },
              error: function (err) {
                  console.log(err)
              }

            });

        });

          },

        error: function (err) {
            console.log(err)
        }
      });
        


});

