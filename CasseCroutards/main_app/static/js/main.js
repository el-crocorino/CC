function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function crsfSafeMethod(method) {
    // No csrf protection needed for these methods
    return(/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

/*
 * Appends html form to add tripItem, updates tripItem counter
 *
 * @param DOMObject pDivElement  Div wheer html form will be append to
 * @param string pPrefix Form prefix
 * @param iut pTripItemCounter Trip items count
 * @param string pTripitemForm Trip item add form
 */
function addTripItem( pDivElement, pPrefix, pTripItemCounter, pTripItemForm) {

    pDivElement.append('<hr />');

    var formDivId = pPrefix + '-' + pTripItemCounter;

    pDivElement.append(`<div id="` + formDivId + `">` + pTripItemForm + `</div>`);
    //pDivElement.append(`<button type="button" id="deleteTripItem" >{% trans "deleteTripItem" %}</button>`);
    
    $.each( $( '#' + formDivId + ' label'), function( pIndex, pElement) {

        var newName = pPrefix + pTripItemCounter + '-' + pElement.htmlFor.substring( pPrefix.length + 4);
        var newId = 'id_' + newName;

        $( '#' + pElement.htmlFor).attr( 'id', newId).attr( 'name', newName);
        pElement.htmlFor = newId;

    });

    var idFieldNewName = pPrefix + pTripItemCounter + '-id';

    $( '#id_' + pPrefix + '-id').attr( 'id', 'id_' + idFieldNewName).attr( 'name', idFieldNewName).val( 'new');
        
    return ++pTripItemCounter;


}

/*
 * Deletes tripItem and removes corresponding html
 *
 * @param DOMObject pElement Button who called function, containing trip item id
 */
function deleteTripItem( pElement) {

    var itemId = pElement.attr("data-id");

    $.ajax({
        url: '/tripItem/delete/',
        type: 'POST',
        data: {"itemId" : itemId},
        success: function(response){
            success: function(response){
                $('#tripItem-' + itemId).html(' ' + response);
            }
        }
    });

}


                

var csrftoken = getCookie('csrftoken');

$.ajaxSetup({
    beforeSend: function( xhr, settings) {
        if( ! crsfSafeMethod(settings.type) && ! this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken)
        }
    }
});

/*$('button').on('click', function(event) {

    event.preventDefault();
    var element = $(this);

    $.ajax({
        url: '/like_treasure/',
        type: 'POST',
        data: {treasure_id : element.attr("data-id")},
        success: function(response){
            element.html(' ' + response);
        }
    });

});*/