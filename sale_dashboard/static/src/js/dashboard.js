odoo.define('sale_dashboard.dashboard', function(require){
"user strict";

var AbstractAction = require('web.AbstractAction');
var core = require('web.core');
var field_utils = require('web.field_utils');
var QWeb = core.qweb;


var dashboard2 = AbstractAction.extend({
    contentTemplate: 'SaleTemplate',

    events : {
        "click .button_clickable": function (){
            var self = this
            var sale = this._rpc({
                model: 'sale.order',
                method: 'sale_count',
                args: [
                        [],]
            })
            .then(function(result){
                self.$el.html(QWeb.render('backend_dash',{'product': result}));
            });
        }
    }

});
    core.action_registry.add('sale_backend_dashboard', dashboard2);
    return dashboard2;

});
