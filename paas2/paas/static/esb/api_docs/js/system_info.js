// system info render

$(function () {
    var NavView = Backbone.View.extend({
        el: '#system_api_info',
        api_list_template: Handlebars.compile($('#tmpl-api-list-content').html()),
        events: {
            'click #system_desc': function () {
                this.init_desc_content();
            },
            'click .sub-menu a': 'render_right_content',
            'click #all_api_info a': 'jump_the_api_docs',
        },
        initialize: function (ev) {
            this.init_left_nav();
            this.render_right_content();
        },
        init_left_nav: function (ev) {
            var menu = $('.has_submenu>a').parent("li");
            var sunMenu = $('.has_submenu>a').next("ul");
            $(".navi > li > ul").slideUp(350);

            setTimeout(function(){
                $(".navi > li").removeClass("open");
                sunMenu.slideDown(350);
                menu.addClass("open");
            },350);
            $(".has_submenu > a").click(function(e) {
                var menu = $(this).parent("li");
                var sunMenu = $(this).next("ul");
                if (menu.hasClass("open")) {
                    sunMenu.slideUp(350,function(){
                        menu.removeClass("open");
                    });
                } else {
                    $(".navi > li > ul").slideUp(350);
                    setTimeout(function(){
                        $(".navi > li").removeClass("open");
                        sunMenu.slideDown(350);
                        menu.addClass("open");
                    },350);
                }
                return false;
            });
        },
        render_right_content: function () {
            //处理面包屑
            var name = $('.a-active-style').attr('name');
            if(name!='desc'){
                $("#curr_breadcrumb").empty().html(gettext('API列表') + ' > '+name);
            }else{
                $("#curr_breadcrumb").empty().html(gettext('简介'));
                this.init_desc_content();
            }
        },
        init_desc_content: function(ev){
            var tmpl = this.api_list_template;
            $.get(desc_content_url,function (data) {
                $('#right-content').empty().html(tmpl(data));
            });
        },
        jump_the_api_docs: function (ev) {
            //组装请求路径
            var api_name = $(ev.currentTarget).attr('name');
            //url = root_url+api_name+'/';  root_url bug，被修改，没有系统部分
            url = window.location.pathname +api_name+'/';
            window.location.href=url;
        }
    });

    window.nav_view = new NavView();
});
