%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dmm
%global packver   3.2-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Dyadic Mixed Model for Pedigree Data

License:          GPL-2 | GPL (>= 2) | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-CRAN-nadiv 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-pls 
Requires:         R-CRAN-nadiv 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Mixed model analysis for quantitative genetics with multi-trait responses
and pedigree-based partitioning of individual variation into a range of
environmental and genetic variance components for individual and maternal
effects. Method documented in dmmOverview.pdf; dmm is an implementation of
dispersion mean model described by Searle et al. (1992) "Variance
Components", Wiley, NY. 'DMM' can do 'MINQUE', 'bias-corrected-ML', and
'REML' variance and covariance component estimates.

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
