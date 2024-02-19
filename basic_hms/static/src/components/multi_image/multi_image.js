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
      before: [],
      options: {},
    });

    onWillStart(() => this.loadImage());

    onMounted(() => {
      // if (this.state.images.length < 2) {
      //   return;
      // }
      // const images = this.state.images
      //   .sort((a, b) => a.sequence - b.sequence)
      //   .map((item) => item.image_1920);
      // $(".thumb-item").brazzersCarousel();
    });
  }

  async loadImage() {
    const before_ids = this.props.record.data.before_image_ids.resIds;
    this.state.before = await this.orm.searchRead(
      "multi.image",
      [["id", "in", before_ids]],
      ["name", "image_1920", "sequence"],
      { order: "sequence asc" }
    );
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
  console.log(attrs.options);
  return {
    multiOptions: attrs.options,
  };
};

MultiImage.displayName = "";
MultiImage.supportedTypes = ["binary"];

registry.category("fields").add("multi_image", MultiImage);
