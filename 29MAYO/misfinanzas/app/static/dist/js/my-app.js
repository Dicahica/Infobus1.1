var app = new Framework7({
  // App root element
  root: '#app',
  // App Name
  name: 'My App',
  // App id
  id: 'com.myapp.test',
  // Enable swipe panel
  panel: {
    swipe: 'left',
  },
  // Add default routes
  routes: [
    {
      path: '/about/',
      url: 'about.html',
    },
  ],
  // ... other parameters
});


var $$ = Dom7;

// Dom Events
$$('.panel-left').on('panel:open', function () {
  console.log('Panel left: open');
});
$$('.panel-left').on('panel:opened', function () {
  console.log('Panel left: opened');
});


// App Events
app.on('panelClose', function (panel) {
  console.log('Panel ' + panel.side + ': close');
});
app.on('panelClosed', function (panel) {
  console.log('Panel ' + panel.side + ': closed');
});
var mainView = app.views.create('.view-main');

// DOM events for About popup
$$('.popup-about').on('popup:open', function (e, popup) {
  console.log('About popup open');
});
$$('.popup-about').on('popup:opened', function (e, popup) {
  console.log('About popup opened');
});

// Create dynamic Popup
var dynamicPopup = app.popup.create({
  content: '<div class="popup">'+
              '<div class="block">'+
                '<p>Popup created dynamically.</p>'+
                '<p><a href="#" class="link popup-close">Close me</a></p>'+
              '</div>'+
            '</div>',
  // Events
  on: {
    open: function (popup) {
      console.log('Popup open');
    },
    opened: function (popup) {
      console.log('Popup opened');
    },
  }
});
// Events also can be assigned on instance later
dynamicPopup.on('close', function (popup) {
  console.log('Popup close');
});
dynamicPopup.on('closed', function (popup) {
  console.log('Popup closed');
});

// Open dynamic popup
$$('.dynamic-popup').on('click', function () {
  dynamicPopup.open();
});


// DOM events for my-sheet sheet
$$('.my-sheet').on('sheet:open', function (e, sheet) {
  console.log('my-sheet open');
});
$$('.my-sheet').on('sheet:opened', function (e, sheet) {
  console.log('my-sheet opened');
});

// Create dynamic Sheet
var dynamicSheet = app.sheet.create({
  content: '<div class="sheet-modal">'+
              '<div class="toolbar">'+
                '<div class="toolbar-inner">'+
                  '<div class="left"></div>'+
                  '<div class="right">'+
                    '<a class="link sheet-close">Done</a>'+
                  '</div>'+
                '</div>'+
              '</div>'+
              '<div class="sheet-modal-inner">'+
                '<div class="block">'+
                  '<p>Nombre cuenta: </p>'+
                  '<p>Número cuenta: </p>'+
                  '<p>Descripción: </p>'+
                  '<p>DSaldo: </p>'+
                  '<p>Tipo: </p>'+
                  '<p><a href="#" class="link sheet-close">cerrar</a></p>'+
                '</div>'+
              '</div>'+
            '</div>',
  // Events
  on: {
    open: function (sheet) {
      console.log('Sheet open');
    },
    opened: function (sheet) {
      console.log('Sheet opened');
    },
  }
});
// Events also can be assigned on instance later
dynamicSheet.on('close', function (sheet) {
  console.log('Sheet close');
});
dynamicSheet.on('closed', function (sheet) {
  console.log('Sheet closed');
});

// Open dynamic sheet
$$('.dynamic-sheet').on('click', function () {
  // Close inline sheet before
  app.sheet.close('.my-sheet');

  // Open dynamic sheet
  dynamicSheet.open();
});

var calendarDateFormat = app.calendar.create({
  inputEl: '#demo-calendar-date-format',
  dateFormat: 'MM dd yyyy'
});

var calendarDateFormat = app.calendar.create({
  inputEl: '#demo-calendar-date-format2',
  dateFormat: 'MM dd yyyy'
});

// Dom Events
$$('.panel-left').on('panel:open', function () {
  console.log('Panel left: open');
});
$$('.panel-left').on('panel:opened', function () {
  console.log('Panel left: opened');
});


// App Events
app.on('panelClose', function (panel) {
  console.log('Panel ' + panel.side + ': close');
});
app.on('panelClosed', function (panel) {
  console.log('Panel ' + panel.side + ': closed');
});
var mainView = app.views.create('.view-main');

// DOM events for About popup
$$('.popup-about').on('popup:open', function (e, popup) {
  console.log('About popup open');
});
$$('.popup-about').on('popup:opened', function (e, popup) {
  console.log('About popup opened');
});

// Create dynamic Popup
var dynamicPopup = app.popup.create({
  content: '<div class="popup">'+
              '<div class="block">'+
                '<p>Popup created dynamically.</p>'+
                '<p><a href="#" class="link popup-close">Close me</a></p>'+
              '</div>'+
            '</div>',
  // Events
  on: {
    open: function (popup) {
      console.log('Popup open');
    },
    opened: function (popup) {
      console.log('Popup opened');
    },
  }
});
// Events also can be assigned on instance later
dynamicPopup.on('close', function (popup) {
  console.log('Popup close');
});
dynamicPopup.on('closed', function (popup) {
  console.log('Popup closed');
});

// Open dynamic popup
$$('.dynamic-popup').on('click', function () {
  dynamicPopup.open();
});

var toggle = app.toggle.get('.toggle');



// Set progress on inline progressbar
$$('.set-inline-progress').on('click', function (e) {
  var progress = $$(this).attr('data-progress');
  app.progressbar.set('#demo-inline-progressbar', progress);
});


// Function show determinate progressbar and emulate loading
determinateLoading = false;
function showDeterminate(inline) {
  determinateLoading = true;
  var progressBarEl;
  if (inline) {
    // inline progressbar
    progressBarEl = app.progressbar.show('#demo-determinate-container', 0);
  } else {
    // root progressbar
    progressBarEl = app.progressbar.show(0, app.theme === 'md' ? 'yellow' : 'blue');
  }
  var progress = 0;
  function simulateLoading() {
    setTimeout(function () {
      var progressBefore = progress;
      progress += Math.random() * 20;
      app.progressbar.set(progressBarEl, progress);
      if (progressBefore < 100) {
        simulateLoading(); //keep "loading"
      }
      else {
        determinateLoading = false;
        app.progressbar.hide(progressBarEl); //hide
      }
    }, Math.random() * 200 + 200);
  }
  simulateLoading();
}
// show inline determinate progressbar
$$('.show-determinate').on('click', function (e) {
  showDeterminate(true);
});

// show root determinate progressbar
$$('.show-determinate-root').on('click', function (e) {
  showDeterminate(false);
});

var infiniteLoading = false;
// show inline infinite progressbar
$$('.show-infinite').on('click', function () {
  app.progressbar.show(app.theme === 'md' ? 'yellow' : 'blue');
  setTimeout(function () {
    infiniteLoading = false;
    app.progressbar.hide();
  }, 3000);
});

// show root infinite progressbar
$$('.show-infinite-root').on('click', function () {
  app.progressbar.show('multi');
  setTimeout(function () {
    infiniteLoading = false;
    app.progressbar.hide();
  }, 3000);
});

var searchbar = app.searchbar.create({
  el: '.searchbar',
  searchContainer: '.list',
  searchIn: '.item-title',
  on: {
    search(sb, query, previousQuery) {
      console.log(query, previousQuery);
    }
  }
});
