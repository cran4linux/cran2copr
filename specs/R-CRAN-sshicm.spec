%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sshicm
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Information Consistency-Based Measures for Spatial Stratified Heterogeneity

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-sdsfun >= 0.5.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppThread 
Requires:         R-CRAN-sdsfun >= 0.5.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-sf 

%description
Spatial stratified heterogeneity (SSH) denotes the coexistence of
within-strata homogeneity and between-strata heterogeneity. Information
consistency-based methods provide a rigorous approach to quantify SSH and
evaluate its role in spatial processes, grounded in principles of
geographical stratification and information theory (Bai, H. et al. (2023)
<doi:10.1080/24694452.2023.2223700>; Wang, J. et al. (2024)
<doi:10.1080/24694452.2023.2289982>).

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
