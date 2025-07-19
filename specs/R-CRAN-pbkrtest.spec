%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pbkrtest
%global packver   0.5.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.5
Release:          1%{?dist}%{?buildtag}
Summary:          Parametric Bootstrap, Kenward-Roger and Satterthwaite Based Methods for Test in Mixed Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-doBy >= 4.6.22
BuildRequires:    R-CRAN-Matrix >= 1.2.3
BuildRequires:    R-CRAN-lme4 >= 1.1.31
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-CRAN-doBy >= 4.6.22
Requires:         R-CRAN-Matrix >= 1.2.3
Requires:         R-CRAN-lme4 >= 1.1.31
Requires:         R-CRAN-broom 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-CRAN-numDeriv 

%description
Computes p-values based on (a) Satterthwaite or Kenward-Rogers degree of
freedom methods and (b) parametric bootstrap for mixed effects models as
implemented in the 'lme4' package. Implements parametric bootstrap test
for generalized linear mixed models as implemented in 'lme4' and
generalized linear models. The package is documented in the paper by
Halekoh and Højsgaard, (2012, <doi:10.18637/jss.v059.i09>).  Please see
'citation("pbkrtest")' for citation details.

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
