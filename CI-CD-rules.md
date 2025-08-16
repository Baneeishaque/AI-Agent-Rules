* Use Render CLI to trigger deployments manually under Render Cloud Application Platform.
* On Render Cloud Application Platform Deploys: Instruct to set an API key secret (e.g., RENDER_API_KEY) so commands can run non-interactively. Read RENDER_API_KEY from configuration file under a private repo - configured via. Secrets.
* On Render Cloud Application Platform Deploys: Instruct to setup DNS automation - If re-create the service and the onrender.com host changes, Fetch the current external URL at deploy time (env) and update DNS via provider API (Cloudflare/Route53).
* On Render Cloud Application Platform Deploys: Calls “create deploy” on the service and uses a “--wait” flag to block until complete.
