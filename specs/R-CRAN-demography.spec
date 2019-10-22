%global packname  demography
%global packver   1.22
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.22
Release:          1%{?dist}
Summary:          Forecasting Mortality, Fertility, Migration and Population Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast >= 8.5
BuildRequires:    R-CRAN-ftsa >= 4.8
BuildRequires:    R-CRAN-rainbow 
BuildRequires:    R-CRAN-cobs 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-strucchange 
BuildRequires:    R-CRAN-RCurl 
Requires:         R-CRAN-forecast >= 8.5
Requires:         R-CRAN-ftsa >= 4.8
Requires:         R-CRAN-rainbow 
Requires:         R-CRAN-cobs 
Requires:         R-mgcv 
Requires:         R-CRAN-strucchange 
Requires:         R-CRAN-RCurl 

%description
Functions for demographic analysis including lifetable calculations;
Lee-Carter modelling; functional data analysis of mortality rates,
fertility rates, net migration numbers; and stochastic population
forecasting.

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
