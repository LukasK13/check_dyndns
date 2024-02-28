Plugin for checking a dyndns server with Icinga2

# Requirements
* No special requirements 🥳

# Usage

* **-d / --domain** The domain to check.

# Icinga2 config
## Comand template
```
object CheckCommand "dyndns" {
    import "plugin-check-command"
    command = [ PluginDir + "/check_dyndns.py" ]
    arguments += {
        "-d" = {
            description = "The domain to check."
            required = true
            value = "$dyndns_domain$"
        }
    }
}
```

## Service template
```
template Service "check-dyndns" {
    check_command = "dyndns"
    command_endpoint = host_name
}
