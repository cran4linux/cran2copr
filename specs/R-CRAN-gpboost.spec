%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gpboost
%global packver   1.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Combining Tree-Boosting with Gaussian Process and Mixed Effects Models

License:          Apache License (== 2.0) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-R6 >= 2.0
BuildRequires:    R-CRAN-data.table >= 1.9.6
BuildRequires:    R-CRAN-Matrix >= 1.1.0
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-RJSONIO 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-R6 >= 2.0
Requires:         R-CRAN-data.table >= 1.9.6
Requires:         R-CRAN-Matrix >= 1.1.0
Requires:         R-graphics 
Requires:         R-CRAN-RJSONIO 
Requires:         R-methods 
Requires:         R-utils 

%description
An R package that allows for combining tree-boosting with Gaussian process
and mixed effects models. It also allows for independently doing
tree-boosting as well as inference and prediction for Gaussian process and
mixed effects models. See <https://github.com/fabsig/GPBoost> for more
information on the software and Sigrist (2022, JMLR)
<https://www.jmlr.org/papers/v23/20-322.html> and Sigrist (2023, TPAMI)
<doi:10.1109/TPAMI.2022.3168152> for more information on the methodology.

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
