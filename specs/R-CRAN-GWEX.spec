%global packname  GWEX
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Multi-Site Stochastic Models for Daily Precipitation andTemperature

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-EnvStats 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-fGarch 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-Renext 
BuildRequires:    R-CRAN-lmomco 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-EnvStats 
Requires:         R-MASS 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-fGarch 
Requires:         R-parallel 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-Renext 
Requires:         R-CRAN-lmomco 
Requires:         R-methods 
Requires:         R-stats 

%description
Application of multi-site models for daily precipitation and temperature
data. This package is designed for an application to 105 precipitation and
26 temperature gauges located in Switzerland. It applies fitting
procedures and provides weather generators described in the following
references: - Evin, G., A.-C. Favre, and B. Hingray. (2018)
<doi:10.5194/hess-22-655-2018>. - Evin, G., A.-C. Favre, and B. Hingray.
(2018) <doi:10.1007/s00704-018-2404-x>.

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
%{rlibdir}/%{packname}/libs
