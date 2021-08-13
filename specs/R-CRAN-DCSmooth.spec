%global __brp_check_rpaths %{nil}
%global packname  DCSmooth
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Nonparametric Regression and Bandwidth Selection for Spatial Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-fracdiff 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-fracdiff 
Requires:         R-stats 

%description
Nonparametric smoothing techniques for data on a lattice and functional
time series. Smoothing is done via kernel regression or local polynomial
regression, a bandwidth selection procedure based on an iterative plug-in
algorithm is implemented. This package allows for modeling a dependency
structure of the error terms of the nonparametric regression model.
Methods used in this paper are described in Beran/Feng (2002)
<doi:10.1198/106186002420>, Mueller/Wang (1994) <doi:10.2307/2533197>,
Feng/Schaefer (2021) <https://ideas.repec.org/p/pdn/ciepap/144.html>,
Schaefer/Feng (2021) <https://ideas.repec.org/p/pdn/ciepap/143.html>.

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
