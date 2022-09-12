from django.utils.safestring import mark_safe

from wagtail import hooks


@hooks.register('insert_global_admin_js', order=100)
def global_admin_js():
    return mark_safe(
        """
            <script type="text/javascript">
                $("body").on("DOMNodeInserted", ".jscolor", function (e) {
                    jscolor.install();
                });
                $(document).ready(function(){
                    $(".jscolor").each((item, element)=>{
                        if(element.jscolor){element.jscolor.fromString(element.value);}
                    })
                });
            </script>
        """,
    )
