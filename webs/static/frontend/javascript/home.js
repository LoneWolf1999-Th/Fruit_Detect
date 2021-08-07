function scrollToTop() {
  var position = document.body.scrollTop || document.documentElement.scrollTop;
  if (position) {
    window.scrollBy(0, -Math.max(10, Math.floor(position / 10)));
    scrollAnimation = setTimeout("scrollToTop()", 14);
  } else clearTimeout(scrollAnimation);
}

$(document).ready(function () {
  $("li.home").css({ opacity: "0.5", "pointer-events": "none" });

  // trending-ads-slide
  $(".trending-ads-slide").slick({
    dots: false,
    arrows: false,
    slidesToShow: 3,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 800,
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 1,
          infinite: true,
          dots: false,
        },
      },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 1,
        },
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
        },
      },
      // You can unslick at a given breakpoint now by adding:
      // settings: "unslick"
      // instead of a settings object
    ],
  }); //////////////////////////////

  // $("#popover-content-insect").hide();
  // $(".pop")
  //   .popover({
  //     trigger: "manual",
  //     html: true,
  //     animation: false,
  //     placement: "right",
  //     content: function () {
  //       return $("#popover-content-insect").html();
  //     },
  //   })
  //   .on("mouseenter", function () {
  //     var _this = this;
  //     $(this).popover("show");
  //     $(".popover").on("mouseleave", function () {
  //       $(_this).popover("hide");
  //     });
  //   })
  //   .on("mouseleave", function () {
  //     var _this = this;
  //     setTimeout(function () {
  //       if (!$(".popover:hover").length) {
  //         $(_this).popover("hide");
  //       }
  //     }, 0);
  //   });

  /***************** POPOVER */
  $(".popDisease")
    .popover({
      trigger: "manual",
      html: true,
      animation: false,
      placement: function () {
        if ($(window).width() <= 768) {
          return "top";
        } else {
          return "right";
        }
      },
      content: function () {
        return $("#popover-content-disaese").html();
      },
    })
    .on("mouseenter", function () {
      var _this = this;
      $(this).popover("show");
      $(".popover").on("mouseleave", function () {
        $(_this).popover("hide");
      });
    })
    .on("mouseleave", function () {
      var _this = this;
      setTimeout(function () {
        if (!$(".popover:hover").length) {
          $(_this).popover("hide");
        }
      }, 0);
    });

  $(".popInsect")
    .popover({
      trigger: "manual",
      html: true,
      animation: false,
      placement: function () {
        if ($(window).width() <= 768) {
          return "top";
        } else {
          return "right";
        }
      },
      content: function () {
        return $("#popover-content-insect").html();
      },
    })
    .on("mouseenter", function () {
      var _this = this;
      $(this).popover("show");
      $(".popover").on("mouseleave", function () {
        $(_this).popover("hide");
      });
    })
    .on("mouseleave", function () {
      var _this = this;
      setTimeout(function () {
        if (!$(".popover:hover").length) {
          $(_this).popover("hide");
        }
      }, 0);
    });

  $(".popWater")
    .popover({
      trigger: "manual",
      html: true,
      animation: false,
      placement: function () {
        if ($(window).width() <= 768) {
          return "top";
        } else {
          return "right";
        }
      },
      content: function () {
        return $("#popover-content-water").html();
      },
    })
    .on("mouseenter", function () {
      var _this = this;
      $(this).popover("show");
      $(".popover").on("mouseleave", function () {
        $(_this).popover("hide");
      });
    })
    .on("mouseleave", function () {
      var _this = this;
      setTimeout(function () {
        if (!$(".popover:hover").length) {
          $(_this).popover("hide");
        }
      }, 0);
    });

  $(".popSoil")
    .popover({
      trigger: "manual",
      html: true,
      animation: false,

      placement: function () {
        if ($(window).width() <= 768) {
          return "top";
        } else {
          return "left";
        }
      },
      content: function () {
        return $("#popover-content-soil").html();
      },
    })
    .on("mouseenter", function () {
      var _this = this;
      $(this).popover("show");
      $(".popover").on("mouseleave", function () {
        $(_this).popover("hide");
      });
    })
    .on("mouseleave", function () {
      var _this = this;
      setTimeout(function () {
        if (!$(".popover:hover").length) {
          $(_this).popover("hide");
        }
      }, 0);
    });
});
