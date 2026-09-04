import { Container } from "cloudflare:containers";

export class VetProofContainer extends Container {
  defaultPort = 8080;
  sleepAfter = "10m";
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const container = env.VETPROOF_CONTAINER.getByName("vetproof-demo");
    return container.fetch(new Request(url, request));
  },
};
