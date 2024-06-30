/************* Main Js File ************************
    Template Name: jobmaster - Job Board HTML Template
    Author: Theme-House
    Version: 1.0
    Copyright 2024
*************************************************************/


/*------------------------------------------------------------------------------------
    
JS INDEX
=============

01 - Sticky Header
02 - Darepicker Setup
03 - Dropdown Arrow
04 - Slider
05 - Select-2
06 - Responsive Menu
07 - Testimonial SLider
08 - Btn To Top
09 -multiple select
10 - Attach resume


-------------------------------------------------------------------------------------*/


(function ($) {
	"use strict";

	jQuery(document).ready(function ($) {

	
   /* 
		=================================================================
		01 -Sticky Header
		=================================================================	
		*/

        $(window).on('scroll', function () {
            var scroll = $(window).scrollTop();
            if (scroll >= 50) {
                $(".forsticky").addClass("sticky");
            } else {
                $(".forsticky").removeClass("sticky");
                $(".forsticky").addClass("");
            }
        });




		/* 
		=================================================================
		02 - Darepicker Setup
		=================================================================	
		*/

		$(function () {
			$('.datepicker').datepicker({
				format: 'mm-dd-yyyy'
			});
		});

		/* 
		=================================================================
		03 - Dropdown Arrow
		=================================================================	
		*/

		if ($(".dropdown-menu li").length) {
			$(".dropdown-menu li").on('click', function () {
				$(this).parents(".dropdown").find('.btn-dropdown').html($(this).text());
				$(this).parents(".dropdown").find('.btn-dropdown').val($(this).data('value'));
			});
		};

		/* 
			=================================================================
			04 - Slider
			================================================================= 
			*/


			$('.owl-carousel').owlCarousel({
				stagePadding: 0,
				autoplay: true,
				loop: true,
				margin: 10,
				nav: false,
				responsive: {
					0: {
						items: 1
					},
					600: {
						items: 1
					},
					1000: {
						items: 3
					}
				}
			});




		/* 
		=================================================================
		05 - Select-2
		=================================================================	
		*/


		$('.banner-select').select2()

		$('.sidebar-category-select').select2({
			placeholder: 'e.g. job title'
		});
		$('.sidebar-category-select-2').select2({
			placeholder: 'Choose Category'
		});


		/* 
		=================================================================
		06 - Responsive Menu
		=================================================================	
		*/
		$("ul#jobmaster_navigation").slicknav({
			prependTo: ".jobmaster-responsive-menu"
		});



	


		/* 
		=================================================================
		07 - Testimonial SLider
		=================================================================	
		*/
		$(".happy-freelancer-slider").owlCarousel({
			autoplay: true,
			loop: true,
			margin: 20,
			touchDrag: true,
			mouseDrag: true,
			nav: false,
			dots: true,
			autoplayTimeout: 5000,
			autoplaySpeed: 1200,
			autoplayHoverPause: true,
			responsive: {
				0: {
					items: 1
				},
				480: {
					items: 1
				},
				600: {
					items: 1
				},
				750: {
					items: 2
				},
				1000: {
					items: 3
				},
				1200: {
					items: 3
				}
			}
		});


	});

	

	   /* 
		=================================================================
		08 - Btn To Top
		=================================================================	
		*/
        if ($("body").length) {
            var btnUp = $('<div/>', {
                'class': 'btntoTop'
            });
            btnUp.appendTo('body');
            $(document).on('click', '.btntoTop', function () {
                $('html, body').animate({
                    scrollTop: 0
                }, 700);
            });
            $(window).on('scroll', function () {
                if ($(this).scrollTop() > 200) $('.btntoTop').addClass('active');
                else $('.btntoTop').removeClass('active');
            });
        }




         /* 
		=================================================================
		09 -multiple select
		=================================================================	
		*/
  $(document).ready(function() {
    $(".sd-CustomSelect").multipleSelect({
      selectAll: false,
      onOptgroupClick: function(view) {
        $(view).parents("label").addClass("selected-optgroup");
      }
    });
  });

    $(document).ready(function() {
    $(".sd-CustomSelect_2").multipleSelect({
      selectAll: false,
      onOptgroupClick: function(view) {
        $(view).parents("label").addClass("selected-optgroup");
      }
    });
  });

      $(document).ready(function() {
    $(".sd-CustomSelect_3").multipleSelect({
      selectAll: false,
      onOptgroupClick: function(view) {
        $(view).parents("label").addClass("selected-optgroup");
      }
    });
  });

  /* 
		=================================================================
		10 - Attach resume
		=================================================================	
		*/


const dropArea = document.querySelector(".drop_box"),
  button = dropArea.querySelector("button"),
  dragText = dropArea.querySelector("header"),
  input = dropArea.querySelector("input");
let file;
var filename;

button.onclick = () => {
  input.click();
};

input.addEventListener("change", function (e) {
  var fileName = e.target.files[0].name;
  let filedata = `
    <form action="" method="post">
    <div class="form">
    <h4>${fileName}</h4>
    <input type="email" placeholder="Enter email upload file">
    <button class="btn">Upload</button>
    </div>
    </form>`;
  dropArea.innerHTML = filedata;
});



}(jQuery));

  