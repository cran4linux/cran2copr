%global packname  RClimMAWGEN
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          RClimMAWGEN (R Climate Index Multi-site Auto-regressive WeatherGENeretor): a package to generate time series of climateindices from RMAWGEN generations.

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-climdex.pcic 
BuildRequires:    R-CRAN-RMAWGEN 
Requires:         R-CRAN-climdex.pcic 
Requires:         R-CRAN-RMAWGEN 

%description
This package contains wrapper functions and methods which allow to use
"climdex.pcic" and "RMAWGEN" packages.  With this simple approach it is
possible to calculate climate change indices, suggested by the WMO-CCL,
CLIVAR, ETCCDMI(http://www.climdex.org),on stochastic generations of
temperature and precipitation time series, obtained by the application of
RMAWGEN.  Each index can be applied to both observed data and to synthetic
time series produced by the Weather Generator, over a reference period
(e.g. 1981-2010, as in the example). It contains also functions and
methods to evaluate the generated time series of climate change indices
consistency by statistical tests.Bugs/comments/questions/collaboration of
any kind are warmly welcomed.

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
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/INDEX
