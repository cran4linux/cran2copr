%global packname  loggit
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          2%{?dist}
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

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
