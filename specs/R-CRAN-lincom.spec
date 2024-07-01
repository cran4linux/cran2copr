%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lincom
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Linear Biomarker Combination: Empirical Performance Optimization

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-SparseM 
BuildRequires:    R-CRAN-Rmosek 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-SparseM 
Requires:         R-CRAN-Rmosek 
Requires:         R-methods 
Requires:         R-stats 

%description
Perform two linear combination methods for biomarkers: (1) Empirical
performance optimization for specificity (or sensitivity) at a controlled
sensitivity (or specificity) level of Huang and Sanda (2022)
<doi:10.1214/22-aos2210>, and (2) weighted maximum score estimator with
empirical minimization of averaged false positive rate and false negative
rate. Both adopt the algorithms of Huang and Sanda (2022)
<doi:10.1214/22-aos2210>. 'MOSEK' solver is used and needs to be
installed; an academic license for 'MOSEK' is free.

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
