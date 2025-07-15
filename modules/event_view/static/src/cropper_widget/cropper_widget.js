import { ImageField } from "@web/views/fields/image/image_field";
import { registry } from "@web/core/registry";

export class CropperField extends ImageField {
    static template = "event_view.CropperField";
    static props = {
        ...ImageField.props,
        ratio: { type: Number, optional: true },
    };

    static defaultProps = {
        ratio: 1
    }




}

registry.category("fields").add("cropper_image", CropperField);
