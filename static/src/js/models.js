odoo.define('einvs_pos_sa.NewPOSModels', function (require) {
"use strict";
// var core = require('web.core');
//    var _t = core._t;
    var session = require('web.session');
    var chrome = require("point_of_sale.Chrome");
    var register = require("point_of_sale.Registries");
    var gui = require("point_of_sale.Gui");
    var rpc = require('web.rpc');

    var models = require('point_of_sale.models');

//    var core = require('web.core');
//    var _t = core._t;
//    var session = require('web.session');
//    var rpc = require('web.rpc');
//    var exports = {};

//exports.PosModel = Backbone.Model.extend({
//

var _super_order = models.Order.prototype;
models.Order = models.Order.extend({
//    initialize: function() {
//        _super_order.initialize.apply(this,arguments);
//        this.l10n_fr_hash = this.l10n_fr_hash || false;
//        this.save_to_db();
//    },
    export_for_printing: function() {
        debugger;

        var result = _super_order.export_for_printing.apply(this,arguments);


        var qr_enzapps = this.enzapps_custom_call()
    //        console.log(self.manualLines,'self.manualLines')
//        var qr_mounika = self.manualLines
//        result.qr_mounika = qr_mounika
    //        console.log(qr_mounika,'qr_mounika22222222222222')




//      result.l10n_fr_hash = this.get_l10n_fr_hash();
      return result;
    },


    enzapps_custom_call: function(){
             debugger;
              var model = 'pos.order';
            // Use an empty array to search for all the records
            var domain = [];
            // Use an empty array to read all the fields of the records
            var fields = [];
//            var rpc = require('web.rpc')
            self = this
//            this.rpc
            return this.pos.rpc({
                model: model,
                method: 'enzapps_custom_call',
//                args: [[this.name]]
                args: [[this.name]]
//                kwargs: {context: this.name},
//                   model: 'pos.order',
//                            method: 'search_read',
//                            domain: [['pos_reference', '=', this.name]],
//                            fields: ['id'],
            }).then(function (data) {
                debugger;
                console.log(data,'mou')

                var mounika = data
                if (document.getElementById("ItemPreview")) {
                document.getElementById("ItemPreview").src = "data:image/png;base64," + data;
//                document.getElementById("ItemPreview").src = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA4QAAAOEAQAAAADRNcKWAAAFF0lEQVR4nO3dSa7jNhAA0GKQvXyDvv/tpBMwCw0c/TtAEluBHhe/TYvWQ3NVKBbJlOOzbfvjw2AEkUgkEolEIpFIJBKJRCKRSCQSiUQikUgkEolEIpH4LTHy1YZHy/Xd+akbl/PavmC5/oyvOtr6hFklEolEIpF4O7FEI2PYk/MakdKr7f7KOaVXREoppZzXv/Gqx80qkUgkEonEL4l/dv20/7Os5xfLGim2FDmWvH8q4/L+YEuR9++WNfL7V+3tCbNKJBKJRCLxfyFuV55mS3vkUlI0Kf06FqqORM855B+J/3ojEolEIpH4TLHP53TtyM4s+fwTbZ7mTO/kKtHTJ3C69oRZJRKJRCKReAexj3O6spwjatle5xfLGnnvnmtZ3W9T2x3bE2aVSCQSiUTiHcQmztnmq05pL81Z1j2IqbvVn9ykct68Kp4xq0QikUgkEu8gVnHOLP9SiozrIeW7pg45V8tY79sTZpVIJBKJROIdxP78nHofeHXozXBWzlGbvNSn5nRP59vM1yfMKpFIJBKJxDuI/TF/JX55G86UcfNzAuMKcaYB0BNmlUgkEolE4h3EZt2qFNWUT82pOfVCVSlB3l57bXJuT9c5Xtq3J8wqkUgkEonEO4jTpajZ2tN8ySom+Zzl6kb7PvkcIpFIJBKJH22/W3aK61MXv0Q9pA6AypvXepw4h0gkEolE4mdbv9+qPhhwfNAcEfi6dlm9qm5cQ4695n17wqwSiUQikUi8g/jmvvKl7nbLWHX18dqmbbrBWR0ykUgkEonE74l9Piddn448zXn0X2rvfSh5mtT+tj48uQyp7oJ4wqwSiUQikUi8gzjmc5ah0vgYtw7FyLOynlmVsvocIpFIJBKJ383nHG1L0dXnRH3lw9qU3JQinYh3BTlde8KsEolEIpFIvIM4pmjWiPpMwNJm26/W+i3laZ0kUp9DJBKJRCLxO2Lkvq3Xg3VeVXw8X37YhD4bLM4hEolEIpH44dZFOfWjM2PztgxnXovTvX69XiXOIRKJRCKR+NE2W2KaLUrNruYsn364ByurQyYSiUQikfgVcXqP59vLyI/fdN24Bke93DWU5ohziEQikUgkfrQNS1bLEPHMoqCS4yk/m91SXj8V5xCJRCKRSPxoG/I5uQ5YSqwyW8aaH7GzXl8sszc/YVaJRCKRSCTeQezzOT+EM0u7hSommZ1xnDpkIpFIJBKJ3xLH/VZNEmY4RCfa0GWdd91vRSQSiUQi8ftifx5ybj/V3e113nl1tvOM5FzdeXXcg7Xk9lar0p4wq0QikUgkEu8gphLJlAs5u2657aG+rrN5Gu3P4v2Q7QmzSiQSiUQi8WZivT/q7Kb0urprREoppbogJyIitpSOPxEx33U+Fz/UiEQikUgkPlMc95WX1lXWnNHNvD6n+Vl3RrL6HCKRSCQSid+uzxkXoGaLV90K1tv1rei7e3vCrBKJRCKRSLyD2J+fc3w7brWaHwI45m6G16/dnehPmFUikUgkEol3EPv9Vl2r8zRLHcOUPE2uxkWcW7K61FDVfcKsEolEIpFIvIP4mzgn9qhlS+efaDecn3vNh+KeLV2LV92zJ8wqkUgkEonEO4rdZqqUfg3n/6WUUrd7PMq+rPKLo9sP/v7/kUgkEolE4jPE3+y3KkO6wXU8tNR3PNRHIUe494FIJBKJROLXxDSGN/9tc04gkUgkEolEIpFIJBKJRCKRSCQSiUQikUgkEolEIvFB4l9OYKagLR92FwAAAABJRU5ErkJggg==";
            }
            });
            },


});
});
