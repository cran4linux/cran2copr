%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  netpanel
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Maximum Likelihood Estimation Routines for Panel Network Autocorrelation Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.1.0
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-Rcpp >= 1.1.0
Requires:         R-CRAN-RcppArmadillo 
Requires:         R-stats 
Requires:         R-CRAN-Matrix 

%description
A set of maximum likelihood estimation routines for panel network
autocorrelation models. The package contains functionality for fixed and
random effects panel network autocorrelation model, in addition to dynamic
panel network autocorrelation that contains time lags of the response and
networks. Moreover, the package allows for multiple networks to be fitted.
For information on the types of models estimated in this package, please
see Anselin (1988) <doi:10.1007/978-94-015-7799-1>, Cook et al. (2023)
<doi:10.1017/S0003055422000272>, Hays et al. (2010)
<doi:10.1016/j.stamet.2009.11.005>, Lee and Yu (2012)
<doi:10.1111/j.1468-2354.2012.00724.x>, Millo (2014)
<doi:10.1016/j.csda.2013.07.024>, Millo and Piras (2012)
<doi:10.18637/jss.v047.i01>, and Wang and Yu (2015)
<doi:10.1016/j.econlet.2015.01.021>.

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
