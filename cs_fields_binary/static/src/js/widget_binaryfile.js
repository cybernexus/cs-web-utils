
odoo.define('cs_fields_binary.binaryfile_widget', function (require) {
    "use strict";

    var FieldBinaryFile = require("web.basic_fields").FieldBinaryFile;

    FieldBinaryFile.include({
        init: function () {
            this._super.apply(this, arguments);
            if (this.attrs.max_upload_size) {
                if (this.attrs.max_upload_size > 0) {
                    this.max_upload_size = this.attrs.max_upload_size * 1024 * 1024;
                }
            }
        }
    });
});
