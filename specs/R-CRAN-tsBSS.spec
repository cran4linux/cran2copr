%global __brp_check_rpaths %{nil}
%global packname  tsBSS
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Blind Source Separation and Supervised Dimension Reduction for Time Series

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-JADE >= 2.0.2
BuildRequires:    R-CRAN-ICtest >= 0.3.2
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-BSSprep 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-JADE >= 2.0.2
Requires:         R-CRAN-ICtest >= 0.3.2
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-BSSprep 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-boot 
Requires:         R-parallel 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 

%description
Different estimators are provided to solve the blind source separation
problem for multivariate time series with stochastic volatility and
supervised dimension reduction problem for multivariate time series.
Different functions based on AMUSE and SOBI are also provided for
estimating the dimension of the white noise subspace. The package is fully
described in Nordhausen, Matilainen, Miettinen, Virta and Taskinen (2021)
<doi:10.18637/jss.v098.i15>.

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
