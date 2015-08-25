(function () {
  var Application = {};

  Application.Menu = function () {
    this.selector = $('.menu');
    this.iconSelector = $('.menu-open');
    this.closeSelector = this.selector.find('.close');

    this.closeSelector.on('click', function () {
      this.close();
    }.bind(this));

    this.iconSelector.on('click', function () {
      this.open();
    }.bind(this));

  }

  Application.Menu.prototype = {
    close: function () {
      this.selector.fadeOut();
    },

    open: function () {
      this.selector.fadeIn();
    }
  };

  Application.SearchBar = function () {
    this.selector = $('.search'),
    this.inputSelector = this.selector.find('.search-input');
    this.iconSelector = this.selector.find('.search-icon');

    this.iconSelector.on('click', function () {
      this.toggle();
    }.bind(this));
  };

  Application.SearchBar.prototype = {
    toggle: function () {
      this.inputSelector.fadeToggle();
    }
  };

  Application.init = function () {
    var menu = new Application.Menu();
    var searchBar = new Application.SearchBar();
  };

  Application.init();


})()
