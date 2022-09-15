%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RCTS
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Clustering Time Series While Resisting Outliers

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ncvreg 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-cellWise 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-stats 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ncvreg 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-cellWise 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-Rdpack 

%description
Robust Clustering of Time Series (RCTS) has the functionality to cluster
time series using both the classical and the robust interactive fixed
effects framework. The classical framework is developed in Ando & Bai
(2017) <doi:10.1080/01621459.2016.1195743>. The implementation within this
package excludes the SCAD-penalty on the estimations of beta. This robust
framework is developed in Boudt & Heyndels (2022)
<doi:10.1016/j.ecosta.2022.01.002> and is made robust against different
kinds of outliers. The algorithm iteratively updates beta (the
coefficients of the observable variables), group membership, and the
latent factors (which can be common and/or group-specific) along with
their loadings. The number of groups and factors can be estimated if they
are unknown.

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
