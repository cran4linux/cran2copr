%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gam
%global packver   1.22-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.22.1
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Additive Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-stats 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-methods 
Requires:         R-stats 
Requires:         R-splines 
Requires:         R-CRAN-foreach 
Requires:         R-methods 

%description
Functions for fitting and working with generalized additive models, as
described in chapter 7 of "Statistical Models in S" (Chambers and Hastie
(eds), 1991), and "Generalized Additive Models" (Hastie and Tibshirani,
1990).

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
