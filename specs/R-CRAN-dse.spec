%global __brp_check_rpaths %{nil}
%global packname  dse
%global packver   2020.2-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2020.2.1
Release:          3%{?dist}%{?buildtag}
Summary:          Dynamic Systems Estimation (Time Series Package)

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.5.0
Requires:         R-core >= 2.5.0
BuildRequires:    R-CRAN-tframe >= 2007.5.3
BuildRequires:    R-CRAN-setRNG >= 2004.4.1
BuildRequires:    R-CRAN-tfplot 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-tframe >= 2007.5.3
Requires:         R-CRAN-setRNG >= 2004.4.1
Requires:         R-CRAN-tfplot 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Tools for multivariate, linear, time-invariant, time series models. This
includes ARMA and state-space representations, and methods for converting
between them. It also includes simulation methods and several estimation
functions. The package has functions for looking at model roots,
stability, and forecasts at different horizons. The ARMA model
representation is general, so that VAR, VARX, ARIMA, ARMAX, ARIMAX can all
be considered to be special cases. Kalman filter and smoother estimates
can be obtained from the state space model, and state-space model
reduction techniques are implemented. An introduction and User's Guide is
available in a vignette.

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
%{rlibdir}/%{packname}
