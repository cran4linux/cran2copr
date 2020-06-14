%global packname  SPREDA
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          2%{?dist}
Summary:          Statistical Package for Reliability Data Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-survival 
BuildRequires:    R-nlme 
Requires:         R-survival 
Requires:         R-nlme 

%description
The Statistical Package for REliability Data Analysis (SPREDA) implements
recently-developed statistical methods for the analysis of reliability
data. Modern technological developments, such as sensors and smart chips,
allow us to dynamically track product/system usage as well as other
environmental variables, such as temperature and humidity. We refer to
these variables as dynamic covariates. The package contains functions for
the analysis of time-to-event data with dynamic covariates and degradation
data with dynamic covariates. The package also contains functions that can
be used for analyzing time-to-event data with right censoring, and with
left truncation and right censoring. Financial support from NSF and DuPont
are acknowledged.

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
