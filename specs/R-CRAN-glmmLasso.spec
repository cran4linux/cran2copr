%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  glmmLasso
%global packver   1.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.2
Release:          1%{?dist}%{?buildtag}
Summary:          Variable Selection for Generalized Linear Mixed Models by L1-Penalized Estimation

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-minqa 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-GMMBoost 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-stats 
Requires:         R-CRAN-minqa 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-GMMBoost 

%description
A variable selection approach for generalized linear mixed models by
L1-penalized estimation is provided, see Groll and Tutz (2014)
<doi:10.1007/s11222-012-9359-z>. See also Groll and Tutz (2017)
<doi:10.1007/s10985-016-9359-y> for discrete survival models including
heterogeneity.

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
