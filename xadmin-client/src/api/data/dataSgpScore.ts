import { BaseApi } from "@/api/base";
import type { BaseResult, DataListResult } from "@/api/types";

class ModelLabelFieldApi extends BaseApi {
  demoSgp = (params?: object) => {
    return this.request<DataListResult>(
      "get",
      params,
      {},
      `${this.baseApi}/book`
    );
  };
}

export const dataSgpScore = new ModelLabelFieldApi("/api/data");
