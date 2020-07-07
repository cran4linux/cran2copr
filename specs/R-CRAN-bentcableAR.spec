%global packname  bentcableAR
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          3%{?dist}
Summary:          Bent-Cable Regression for Independent Data or AutoregressiveTime Series

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Included are two main interfaces for fitting and diagnosing bent-cable
regressions for autoregressive time-series data or independent data (time
series or otherwise): 'bentcable.ar()' and 'bentcable.dev.plot()'. Some
components in the package can also be used as stand-alone functions. The
bent cable (linear-quadratic-linear) generalizes the broken stick
(linear-linear), which is also handled by this package. Version 0.2
corrects a glitch in the computation of confidence intervals for the CTP.
References that were updated from Versions 0.2.1 and 0.2.2 appear in
Version 0.2.3 and up. Version 0.3.0 improves robustness of the
error-message producing mechanism. It is the author's intention to
distribute any future updates via GitHub.

%prep
%setup -q -c -n %{packname}


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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
