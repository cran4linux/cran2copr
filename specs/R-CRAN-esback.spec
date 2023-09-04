%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  esback
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Expected Shortfall Backtesting

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-esreg 
Requires:         R-CRAN-esreg 

%description
Implementations of the expected shortfall backtests of Bayer and
Dimitriadis (2020) <doi:10.1093/jjfinec/nbaa013> as well as other well
known backtests from the literature. Can be used to assess the correctness
of forecasts of the expected shortfall risk measure which is e.g. used in
the banking and finance industry for quantifying the market risk of
investments. A special feature of the backtests of Bayer and Dimitriadis
(2020) <doi:10.1093/jjfinec/nbaa013> is that they only require forecasts
of the expected shortfall, which is in striking contrast to all other
existing backtests, making them particularly attractive for practitioners.

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
