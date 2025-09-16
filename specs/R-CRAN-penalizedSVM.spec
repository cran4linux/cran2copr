%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  penalizedSVM
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Feature Selection SVM using Penalty Functions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-mlegp 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-tgp 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-mlegp 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-tgp 

%description
Support Vector Machine (SVM) classification with simultaneous feature
selection using penalty functions is implemented. The smoothly clipped
absolute deviation (SCAD), 'L1-norm', 'Elastic Net' ('L1-norm' and
'L2-norm') and 'Elastic SCAD' (SCAD and 'L2-norm') penalties are
available. The tuning parameters can be found using either a fixed grid or
a interval search.

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
