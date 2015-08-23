(function () {
  var Application = {};

  Application.MenuIcon = function () {
    this.selector = $('.menu-open');
  };

  Application.Menu = function () {
    this.selector = $('.menu');
    this.closeSelector = this.selector.find('.close');
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
  };

  Application.SearchBar.prototype = {
    toggle: function () {
      this.searchInput.fadeToggle();
    }
  }

  var menu = new Application.Menu(),
      menuIcon = new Application.MenuIcon(),
      searchBar = new Application.SearchBar();

  menu.closeSelector.on('click', function () {
    menu.close();
  });

  menuIcon.selector.on('click', function () {
    menu.open();
  });

  searchBar.iconSelector.on('click', function () {
    searchBar.inputSelector.toggle();
  });
})()
