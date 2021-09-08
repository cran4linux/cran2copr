%global __brp_check_rpaths %{nil}
%global packname  CSTE
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Covariate Specific Treatment Effect (CSTE) Curve

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.4
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-Rcpp >= 1.0.4
Requires:         R-CRAN-fda 
Requires:         R-splines 
Requires:         R-CRAN-survival 

%description
A uniform statistical inferential tool in making individualized treatment
decisions, which implements the methods of Ma et al.
(2017)<DOI:10.1177/0962280214541724> and Guo et al.
(2021)<DOI:10.1080/01621459.2020.1865167>. It uses a flexible
semiparametric modeling strategy for heterogeneous treatment effect
estimation in high-dimensional settings and can gave valid confidence
bands. Based on it, one can find the subgroups of patients that benefit
from each treatment, thereby making individualized treatment selection.

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
