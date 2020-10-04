%global packname  acmeR
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Implements ACME Estimator of Bird and Bat Mortality by WindTurbines

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildArch:        noarch
BuildRequires:    R-grDevices >= 3.1.1
BuildRequires:    R-graphics >= 3.1.1
BuildRequires:    R-stats >= 3.1.1
BuildRequires:    R-utils >= 3.1.1
BuildRequires:    R-foreign >= 0.8.63
Requires:         R-grDevices >= 3.1.1
Requires:         R-graphics >= 3.1.1
Requires:         R-stats >= 3.1.1
Requires:         R-utils >= 3.1.1
Requires:         R-foreign >= 0.8.63

%description
Implementation of estimator ACME, described in Wolpert (2015), ACME: A
Partially Periodic Estimator of Avian & Chiropteran Mortality at Wind
Turbines (submitted). Unlike most other models, this estimator supports
decreasing-hazard Weibull model for persistence; decreasing search
proficiency as carcasses age; variable bleed-through at successive
searches; and interval mortality estimates. The package provides, based on
search data, functions for estimating the mortality inflation factor in
Frequentist and Bayesian settings.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
