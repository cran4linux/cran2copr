%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mbest
%global packver   0.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.1
Release:          1%{?dist}%{?buildtag}
Summary:          Moment-Based Estimation for Hierarchical Models

License:          Apache License (== 2.0) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-nlme >= 3.1.124
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-bigmemory 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-reformulas 
BuildRequires:    R-CRAN-logging 
Requires:         R-CRAN-nlme >= 3.1.124
Requires:         R-CRAN-abind 
Requires:         R-CRAN-bigmemory 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-reformulas 
Requires:         R-CRAN-logging 

%description
Fast moment-based hierarchical model fitting. Implements methods from the
papers "Fast Moment-Based Estimation for Hierarchical Models," by Perry
(2017) and "Fitting a Deeply Nested Hierarchical Model to a Large Book
Review Dataset Using a Moment-Based Estimator," by Zhang, Schmaus, and
Perry (2018).

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
