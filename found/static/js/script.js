(function () {
  function createTabs(argument) {
    var tabs = $('.tabs-header .tab');
    var tabsContent = $('.tabs-body .tab-content');

    tabs.click(function () {

      var id = $(this).attr('id');
      var contentId = ['#content', id].join('-');

      tabs.removeClass('active');
      $(this).addClass('active');
      tabsContent.removeClass('active');
      $(contentId).addClass('active');
    });
  }
  createTabs();
})()
