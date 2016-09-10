$(document).ready(function() {
    $( ".draggable" ).draggable({
        stack: ".draggable"
    });
    $( "#dock-left" ).droppable({
        drop: function( event, ui ) {
            ui.draggable.attr("id", "drag-left");
            var name = $("#drag-left .poke-name").text();
            var hp = $("#drag-left .hp").text();
            var atk = $("#drag-left .atk").text();
            var def = $("#drag-left .def").text();
            var spatk = $("#drag-left .spatk").text();
            var spdef = $("#drag-left .spdef").text();
            var speed = $("#drag-left .speed").text();
            var ht = $("#drag-left .ht").text();
            var wt = $("#drag-left .wt").text();
            var bmi = $("#drag-left .bmi").text();
            $('#name-left').html(name);
            $('#hp-left').html(hp);
            $('#atk-left').html(atk);
            $('#def-left').html(def);
            $('#spatk-left').html(spatk);
            $('#spdef-left').html(spdef);
            $('#speed-left').html(speed);
            $('#ht-left').html(ht);
            $('#wt-left').html(wt);
            $('#bmi-left').html(bmi);
            $("#drag-left").removeAttr("id");
        }
    });
    $( "#dock-right" ).droppable({
        drop: function( event, ui ) {
            ui.draggable.attr("id", "drag-right");
            var name = $("#drag-right .poke-name").text();
            var hp = $("#drag-right .hp").text();
            var atk = $("#drag-right .atk").text();
            var def = $("#drag-right .def").text();
            var spatk = $("#drag-right .spatk").text();
            var spdef = $("#drag-right .spdef").text();
            var speed = $("#drag-right .speed").text();
            var ht = $("#drag-right .ht").text();
            var wt = $("#drag-right .wt").text();
            var bmi = $("#drag-right .bmi").text();
            $('#name-right').html(name);
            $('#hp-right').html(hp);
            $('#atk-right').html(atk);
            $('#def-right').html(def);
            $('#spatk-right').html(spatk);
            $('#spdef-right').html(spdef);
            $('#speed-right').html(speed);
            $('#ht-right').html(ht);
            $('#wt-right').html(wt);
            $('#bmi-right').html(bmi);
            $("#drag-right").removeAttr("id");
        }
    });
});
