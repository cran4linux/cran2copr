%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RIIM
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Randomization-Based Inference Under Inexact Matching

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-optmatch 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-optmatch 

%description
Randomization-based inference for average treatment effects in potentially
inexactly matched observational studies. It implements the inverse
post-matching probability weighting framework proposed by the authors. The
post-matching probability calculation follows the approach of Pimentel and
Huang (2024) <doi:10.1093/jrsssb/qkae033>. The optimal full matching
method is based on Hansen (2004) <doi:10.1198/106186006X137047>. The
variance estimator extends the method proposed in Fogarty (2018)
<doi:10.1111/rssb.12290> from the perfect randomization settings to the
potentially inexact matching case. Comparisons are made with conventional
methods, as described in Rosenbaum (2002) <doi:10.1007/978-1-4757-3692-2>,
Fogarty (2018) <doi:10.1111/rssb.12290>, and Kang et al. (2016)
<doi:10.1214/15-aoas894>.

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
