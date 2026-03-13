%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fbardl
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Fourier Bootstrap ARDL Cointegration Test

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Implements the Fourier Bootstrap Autoregressive Distributed Lag (FBARDL)
bounds testing approach for cointegration analysis. Combines the Pesaran,
Shin & Smith (2001) <doi:10.1002/jae.616> ARDL bounds testing framework
with Fourier terms to capture structural breaks following Yilanci, Bozoklu
& Gorus (2020) <doi:10.1080/00036846.2019.1686454>, and bootstrap critical
values based on McNown, Sam & Goh (2018)
<doi:10.1080/00036846.2017.1366643> and Bertelli, Vacca & Zoia (2022)
<doi:10.1016/j.econmod.2022.105987>. Features include automatic lag
selection via AIC/BIC, optimal Fourier frequency selection by minimum SSR,
long-run and short-run coefficient estimation, diagnostic tests, and
dynamic multiplier analysis.

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
