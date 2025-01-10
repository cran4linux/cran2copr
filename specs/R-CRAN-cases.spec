%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cases
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Stratified Evaluation of Subgroup Classification Accuracy

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-bindata 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-extraDistr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-bindata 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-extraDistr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-ggplot2 

%description
Enables simultaneous statistical inference for the accuracy of multiple
classifiers in multiple subgroups (strata). For instance, allows to
perform multiple comparisons in diagnostic accuracy studies with
co-primary endpoints sensitivity and specificity (Westphal M, Zapf A.
Statistical inference for diagnostic test accuracy studies with multiple
comparisons. Statistical Methods in Medical Research. 2024;0(0).
<doi:10.1177/09622802241236933>).

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
