Example of site-specific configuration for TE-based test suites
===============================================================

Site-specific configuration may contain sensitive information about
internal network, number of test configurations, regressions schedule
etc and, therefore, is kept private.

The repository provides an example of site-specific configuration with
the best practices on how to define it. It may be used as a reference to
create your site-specific configuration.


# Generic files

``logger.conf`` contains recommended polling and rotation parameters and
defines live log listeners which should be disabled by default. See
listener **name** and **url** parameters which must be customized in
your case. Many log listeners may be defined.
