%global __brp_check_rpaths %{nil}
%global packname  relsurv
%global packver   2.2-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.5
Release:          1%{?dist}%{?buildtag}
Summary:          Relative Survival

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-survival >= 2.42
BuildRequires:    R-CRAN-date 
BuildRequires:    R-splines 
Requires:         R-CRAN-survival >= 2.42
Requires:         R-CRAN-date 
Requires:         R-splines 

%description
Contains functions for analysing relative survival data, including
nonparametric estimators of net (marginal relative) survival, relative
survival ratio, crude mortality, methods for fitting and checking additive
and multiplicative regression models, transformation approach, methods for
dealing with population mortality tables. Work has been described in Pohar
Perme, Pavlic (2018) <doi:10.18637/jss.v087.i08>.

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
