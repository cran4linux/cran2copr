%global __brp_check_rpaths %{nil}
%global packname  loggit
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Modern Logging for the R Ecosystem

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch

%description
An effortless 'ndjson' (newline-delimited 'JSON') logger, with two primary
log-writing interfaces. It provides a set of wrappings for base R's
message(), warning(), and stop() functions that maintain identical
functionality, but also log the handler message to an 'ndjson' log file.
'loggit' also exports its internal 'loggit()' function for powerful and
configurable custom logging. No change in existing code is necessary to
use this package, and should only require additions to fully leverage the
power of the logging system. 'loggit' also provides a log reader for
reading an 'ndjson' log file into a data frame, log rotation, and live
echo of the 'ndjson' log messages to terminal 'stdout' for log capture by
external systems (like containers). 'loggit' is ideal for Shiny apps, data
pipelines, modeling work flows, and more. Please see the vignettes for
detailed example use cases.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
