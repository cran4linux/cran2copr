%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CARM
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Covariate-Adjusted Adaptive Randomization via Mahalanobis-Distance

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-arrangements 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-CRAN-arrangements 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-MASS 

%description
In randomized controlled trial (RCT), balancing covariate is often one of
the most important concern. CARM package provides functions to balance the
covariates and generate allocation sequence by covariate-adjusted Adaptive
Randomization via Mahalanobis-distance (ARM) for RCT. About what ARM is
and how it works please see Y. Qin, Y. Li, W. Ma, H. Yang, and F. Hu
(2024). "Adaptive randomization via Mahalanobis distance" Statistica
Sinica. <doi:10.5705/ss.202020.0440>. In addition, the package is also
suitable for the randomization process of multi-arm trials. For details,
please see Yang H, Qin Y, Wang F, et al. (2023). "Balancing covariates in
multi-arm trials via adaptive randomization" Computational Statistics &
Data Analysis.<doi:10.1016/j.csda.2022.107642>.

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
