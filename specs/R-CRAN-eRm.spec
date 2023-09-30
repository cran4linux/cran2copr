%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  eRm
%global packver   1.0-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Extended Rasch Modeling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-psych 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-MASS 
Requires:         R-splines 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-psych 

%description
Fits Rasch models (RM), linear logistic test models (LLTM), rating scale
model (RSM), linear rating scale models (LRSM), partial credit models
(PCM), and linear partial credit models (LPCM).  Missing values are
allowed in the data matrix.  Additional features are the ML estimation of
the person parameters, Andersen's LR-test, item-specific Wald test,
Martin-Loef-Test, nonparametric Monte-Carlo Tests, itemfit and personfit
statistics including infit and outfit measures, ICC and other plots,
automated stepwise item elimination, simulation module for various binary
data matrices.

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
