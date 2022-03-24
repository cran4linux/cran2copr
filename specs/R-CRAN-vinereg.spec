%global __brp_check_rpaths %{nil}
%global packname  vinereg
%global packver   0.8.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.3
Release:          1%{?dist}%{?buildtag}
Summary:          D-Vine Quantile Regression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-kde1d >= 1.0.2
BuildRequires:    R-CRAN-rvinecopulib >= 0.6.1.1.2
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-BH 
BuildRequires:    R-CRAN-wdm 
BuildRequires:    R-CRAN-RcppThread 
Requires:         R-CRAN-kde1d >= 1.0.2
Requires:         R-CRAN-rvinecopulib >= 0.6.1.1.2
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-assertthat 

%description
Implements D-vine quantile regression models with parametric or
nonparametric pair-copulas. See Kraus and Czado (2017)
<doi:10.1016/j.csda.2016.12.009> and Schallhorn et al. (2017)
<arXiv:1705.08310>.

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
