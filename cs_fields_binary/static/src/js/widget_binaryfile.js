odoo.define('cs_fields_binary.binaryfile_widget', function (require) {
"use strict";

    var FieldBinaryFile = require("web.basic_fields").FieldBinaryFile;

    FieldBinaryFile.include({
        init: function () {
            this._super.apply(this, arguments);
            this.filename_value = this.recordData[this.attrs.filename];
            this.file_size_mb = 25;
            if(this.attrs.filesizemb){
                this.max_upload_size = this.attrs.filesizemb * 1024 * 1024; // filesizemb as integer
            }
        },
    });
});
