/** @odoo-module **/

import { registry } from "@web/core/registry";
import { standardFieldProps } from "@web/views/fields/standard_field_props";
import { Component, useState, onWillStart, useRef, onMounted } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { loadJS, loadCSS } from "@web/core/assets";

export class MultiImage extends Component {
  setup() {
    this.orm = useService("orm");
    this.state = useState({
      images: [],
      options: {},
    });

    onWillStart(() => this.loadImage());

    onMounted(() => {
      if (this.state.images.length < 2) {
        return;
      }
      const images = this.state.images
        .sort((a, b) => a.sequence - b.sequence)
        .map((item) => item.image_1920);
      $("#compare").imgCmp({
        before: `data:image/png;base64,${images[1]}`,
        after: `data:image/png;base64,${images[0]}`,
      });
    });
  }

  async loadImage() {
    // Img Compare
    await loadJS("/basic_hms/static/src/libs/imgcmp/imgcmp.js");

    const ids = this.props.record.data[this.props.multiOptions.ref].resIds;
    const images = await this.orm.searchRead(
      "multi.image",
      [["id", "in", ids]],
      ["name", "image_1920", "sequence"],
      { order: "sequence asc" }
    );
    this.state.images = images;
  }
}

MultiImage.template = "basic_hms.MultiImage";
MultiImage.components = {};

MultiImage.props = {
  ...standardFieldProps,
  multiOptions: { type: Object, optional: true },
};
MultiImage.defaultProps = {
  multiOptions: {},
};

MultiImage.extractProps = ({ attrs }) => {
  console.log(attrs);
  return {
    multiOptions: attrs.options,
  };
};

MultiImage.displayName = "";
MultiImage.supportedTypes = ["binary"];

registry.category("fields").add("multi_image", MultiImage);
