%global __brp_check_rpaths %{nil}
%global packname  PointFore
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Interpretation of Point Forecasts as State-Dependent Quantilesand Expectiles

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gmm 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-sandwich 
Requires:         R-CRAN-gmm 
Requires:         R-boot 
Requires:         R-CRAN-car 
Requires:         R-CRAN-ggplot2 
Requires:         R-MASS 
Requires:         R-stats 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-sandwich 

%description
Estimate specification models for the state-dependent level of an optimal
quantile/expectile forecast. Wald Tests and the test of overidentifying
restrictions are implemented. Plotting of the estimated specification
model is possible. The package contains two data sets with forecasts and
realizations: the daily accumulated precipitation at London, UK from the
high-resolution model of the European Centre for Medium-Range Weather
Forecasts (ECMWF, <https://www.ecmwf.int/>) and GDP growth Greenbook data
by the US Federal Reserve. See Schmidt, Katzfuss and Gneiting (2015)
<arXiv:1506.01917> for more details on the identification and estimation
of a directive behind a point forecast.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
