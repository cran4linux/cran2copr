%global packname  tsBSS
%global packver   0.5.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.7
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
problem for multivariate time series with stochastic volatility
(Matilainen, Nordhausen and Oja (2015) <doi:10.1016/j.spl.2015.04.033>;
Matilainen, Miettinen, Nordhausen, Oja and Taskinen (2017)
<doi:10.17713/ajs.v46i3-4.671>) and supervised dimension reduction problem
for multivariate time series (Matilainen, Croux, Nordhausen and Oja (2017)
<doi:10.1016/j.ecosta.2017.04.002>). Different functions based on AMUSE
and SOBI are also provided for estimating the dimension of the white noise
subspace.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
