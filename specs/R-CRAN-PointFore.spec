%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PointFore
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Interpretation of Point Forecasts as State-Dependent Quantiles and Expectiles

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gmm 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sandwich 
Requires:         R-CRAN-gmm 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-MASS 
Requires:         R-stats 
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
<doi:10.48550/arXiv.1506.01917> for more details on the identification and
estimation of a directive behind a point forecast.

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
