%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fable.intermittent
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Forecasting Models for Intermittent Time Series

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-nloptr >= 2.0.0
BuildRequires:    R-CRAN-tsibble >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-fabletools >= 0.6.0
BuildRequires:    R-CRAN-distributional >= 0.3.0
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-nloptr >= 2.0.0
Requires:         R-CRAN-tsibble >= 1.0.0
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-fabletools >= 0.6.0
Requires:         R-CRAN-distributional >= 0.3.0

%description
Extends the 'fable' framework to support forecasting methods specifically
designed for intermittent time series data, where demand occurs
sporadically with many zero values. All methods produce probabilistic
forecasts returned as 'distributional' objects. The returned forecasts can
be used to evaluate accuracy, plot and print the results seamlessly with
'fable'. The methods include: Harvey, Fernandes (1989)
<doi:10.1080/07350015.1989.10509750>, Willemain, Smart, Schwarz (2004)
<doi:10.1016/S0169-2070(03)00013-X>, Zhou, Viswanathan (2011)
<doi:10.1016/j.ijpe.2010.09.021>, Snyder, Ord, Beaumont (2012)
<doi:10.1016/j.ijforecast.2011.03.009>, Kolassa (2016)
<doi:10.1016/j.ijforecast.2015.12.004>, Hasni, Aguir, Babai, Jemai (2019)
<doi:10.1080/00207543.2018.1424375>, Damato, Azzimonti, Corani (2025)
<doi:10.1016/j.ijforecast.2025.10.001>, Sbrana (2025)
<doi:10.1080/01605682.2025.2569661>.

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
