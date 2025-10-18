%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CovCorTest
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Tests for Covariance and Correlation Matrices and their Structures

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MANOVA.RM 
BuildRequires:    R-CRAN-matrixcalc 
Requires:         R-CRAN-MANOVA.RM 
Requires:         R-CRAN-matrixcalc 

%description
A compilation of tests for hypotheses regarding covariance and correlation
matrices for one or more groups. The hypothesis can be specified through a
corresponding hypothesis matrix and a vector or by choosing one of the
basic hypotheses, while for the structure test, only the latter works.
Thereby Monte-Carlo and Bootstrap-techniques are used, and the respective
method must be chosen, and the functions provide p-values and mostly also
estimators of calculated covariance matrices of test statistics. For more
details on the methodology, see Sattler et al. (2022)
<doi:10.1016/j.jspi.2021.12.001>, Sattler and Pauly (2024)
<doi:10.1007/s11749-023-00906-6>, and Sattler and Dobler (2025)
<doi:10.48550/arXiv.2310.11799>.

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
