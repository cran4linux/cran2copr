%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  flowz
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Local Latent Flow Forecasting with Empirical Calibration

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-fracdiff 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-fracdiff 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 

%description
Fits conditional flow-matching models to univariate time series. Combines
a selectable exponentially weighted moving average (EWMA), autoregressive
integrated moving average (ARIMA), autoregressive fractionally integrated
moving average (ARFIMA), or structural time-series baseline with direct
multi-step residual paths and a random-feature extreme learning machine
(ELM) velocity field. Spectral dispersion calibration uses a chronological
calibration block, with a separate test block for forecast scoring.
Provides simulated forecast paths and smooth marginal distributions.
Methodological background is given by Lipman et al. (2023)
<doi:10.48550/arXiv.2210.02747>, Huang et al. (2006)
<doi:10.1016/j.neucom.2005.12.126>, Hyndman and Khandakar (2008)
<doi:10.18637/jss.v027.i03>, and Haslett and Raftery (1989)
<doi:10.2307/2347679>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
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
