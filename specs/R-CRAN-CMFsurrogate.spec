%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CMFsurrogate
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Calibrated Model Fusion Approach to Combine Surrogate Markers

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
Requires:         R-splines 
Requires:         R-CRAN-MASS 
Requires:         R-stats 

%description
Uses a calibrated model fusion approach to optimally combine multiple
surrogate markers. Specifically, two initial estimates of optimal
composite scores of the markers are obtained; the optimal calibrated
combination of the two estimated scores is then constructed which ensures
both validity of the final combined score and optimality with respect to
the proportion of treatment effect explained (PTE) by the final combined
score. The primary function, pte.estimate.multiple(), estimates the PTE of
the identified combination of multiple surrogate markers. Details are
described in Wang et al (2022) <doi:10.1111/biom.13677>.

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
