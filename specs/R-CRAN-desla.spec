%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  desla
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Desparsified Lasso Inference for Time Series

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-parallelly 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppProgress 
BuildRequires:    R-CRAN-sitmo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Rdpack 
Requires:         R-stats 
Requires:         R-CRAN-parallelly 

%description
Calculates the desparsified lasso as originally introduced in van de Geer
et al. (2014) <doi:10.1214/14-AOS1221>, and provides inference suitable
for high-dimensional time series, based on the long run covariance
estimator in Adamek et al. (2020) <arXiv:2007.10952>. Also estimates
high-dimensional local projections by the desparsified lasso, as described
in Adamek et al. (2022) <arXiv:2209.03218>.

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
