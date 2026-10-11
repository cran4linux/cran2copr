%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ardlverse
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Comprehensive ARDL: Panel, Bootstrap and Fourier Methods

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
A unified framework for Autoregressive Distributed Lag (ARDL) modeling and
cointegration analysis. Implements Panel ARDL with Pooled Mean Group
(PMG), Mean Group (MG), and Dynamic Fixed Effects (DFE) estimators
following Pesaran, Shin and Smith (1999)
<doi:10.1080/01621459.1999.10474156>. Provides the bounds test of Pesaran,
Shin and Smith (2001) <doi:10.1002/jae.616> with the critical values of
Kripfganz and Schneider (2020) <doi:10.1111/obes.12377> and with recursive
bootstrap critical values following Bertelli, Vacca and Zoia (2022)
<doi:10.1016/j.econmod.2022.105987> and McNown, Sam and Goh (2018)
<doi:10.1080/00036846.2017.1366643>. Includes Quantile Nonlinear ARDL
(QNARDL) combining distributional and asymmetric effects based on Shin, Yu
and Greenwood-Nimmo (2014) <doi:10.1007/978-1-4899-8008-3_9>, Fourier ARDL
for modeling smooth structural breaks following Enders and Lee (2012)
<doi:10.1016/j.econlet.2012.04.081>, and Fourier (bootstrap) nonlinear
ARDL. Features include Augmented ARDL (AARDL) with deferred t and F tests,
Multiple-Threshold NARDL for complex asymmetries, Rolling/Recursive ARDL
for time-varying relationships, and Panel NARDL for nonlinear panel
cointegration. All methods include comprehensive diagnostics,
publication-ready outputs, and visualization tools.

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
