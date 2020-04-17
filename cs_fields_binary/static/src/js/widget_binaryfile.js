
odoo.define('cs_fields_binary.binaryfile_widget', function (require) {
"use strict";

    var FieldBinaryFile = require("web.basic_fields").FieldBinaryFile;

    FieldBinaryFile.include({
        init: function () {
            this._super.apply(this, arguments);
            var self = this;
            this.binary_file_settings = this._rpc({
                model: 'binary.field.setting',
                method: 'get_settings',
                args: [self.model, self.name]
            }).then(function(val){
                self.$el.find('input[type="file"]').attr('accept', val.accepted_file_override);
                if(val.file_size_mb > 0){
                    self.max_upload_size = val.file_size_mb * 1024 * 1024;
                }                                 
            });
        }
    });
});
