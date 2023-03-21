// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

var male = 0;
var female = 0;
var gender_data = gender_data;

for (let i = 0; i < gender_data.length; i++) {
   
  if(gender_data[i].gender == "Man"){

      male = gender_data[i].count; 

  }else if(gender_data[i].gender == "Woman"){

      female = gender_data[i].count; 

  }

}

var kid = 0;
var teenage = 0;
var adult = 0;
var elder = 0;

for (let i = 0; i < age_category_data.length; i++) {
   
  if(age_category_data[i].age_category == "Kid"){
    
      male = age_category_data[i].count; 

  }else if(age_category_data[i].age_category == "Teenage"){
  
      teenage = age_category_data[i].count; 

  }else if(age_category_data[i].age_category == "Adult"){
  
      adult = age_category_data[i].count; 

  }else if(age_category_data[i].age_category == "Elder"){
  
      elder = age_category_data[i].count; 

  }

}



// Pie Chart Example
var ctx = document.getElementById("gender-chart");
var myPieChart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ["Male", "Female"],
    datasets: [{
      data: [male, female],
      backgroundColor: ['#430eef', '#e754a5'],
      hoverBackgroundColor: ['#5d38ff', '#f389bd'],
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
    },
    legend: {
      display: false
    },
    cutoutPercentage: 80,
  },
});


// Pie Chart Example
var ctx = document.getElementById("age_group");
var myPieChart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ['Kids', 'Teenagers', 'Adults', 'Elders'],
    datasets: [{
      data: [kid, teenage, adult, elder],
      backgroundColor: ['#0220b7', '#127542','#b2bc24', '#c25012'],
      hoverBackgroundColor: ['#6d7cce', '#169a5b', '#d4db4a', '#e96f3c'],
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
    },
    legend: {
      display: false
    },
    cutoutPercentage: 80,
  },
});

// Pie Chart Example
var ctx = document.getElementById("emotion");
var myPieChart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ['Natural', 'Happy', 'Sad', 'Angery', 'Surprise'],
    datasets: [{
      data: [55, 30,10,40,10],
      backgroundColor: ['#0220b7', '#127542','#030400', '#ee1616', '#81695d', '#386772', '#5ec37c;'],
      hoverBackgroundColor: ['#6d7cce', '#169a5b', '#4b4d4b', '#ff3838', '#a28b7e', '#57849c', '#82e29f'],
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
    },
    legend: {
      display: false
    },
    cutoutPercentage: 80,
  },
});


// Pie Chart Example
var ctx = document.getElementById("mask");
var myPieChart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ["Mask", "Non-Masn"],
    datasets: [{
      data: [55, 30],
      backgroundColor: ['#0220b7', '#f51c0c'],
      hoverBackgroundColor: ['#6d7cce', '#ff5a4d'],
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
    },
    legend: {
      display: false
    },
    cutoutPercentage: 80,
  },
});


// Pie Chart Example
var ctx = document.getElementById("race");
var myPieChart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ['Asian', 'White', 'Black'],
    datasets: [{
      data: [55, 10, 23],
      backgroundColor: ['#0220b7', '#f6e8c3', '#030001'],
      hoverBackgroundColor: ['#6d7cce', '#f9ecd6', '#4b4d4b'],
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
    },
    legend: {
      display: false
    },
    cutoutPercentage: 80,
  },
});




// Pie Chart Example
var ctx = document.getElementById("sentiment_analysis");
var myPieChart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ['Positive', 'Negative'],
    datasets: [{
      data: [55, 70],
      backgroundColor: ['#0220b7', '#fe3737'],
      hoverBackgroundColor: ['#6d7cce', '#ff7070'],
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
    },
    legend: {
      display: false
    },
    cutoutPercentage: 80,
  },
});



