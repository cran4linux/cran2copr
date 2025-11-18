%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SCoRES
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Simultaneous Confidence Region Excursion Sets

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4
Requires:         R-core >= 4.4
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-metR 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-refund 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-metR 
Requires:         R-CRAN-nlme 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-refund 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-magrittr 
Requires:         R-utils 

%description
Provides computational tools for estimating inverse regions and
constructing the corresponding simultaneous outer and inner confidence
regions. Acceptable input includes both one-dimensional and
two-dimensional data for linear, logistic, functional, and spatial
generalized least squares regression models. Functions are also available
for constructing simultaneous confidence bands (SCBs) for these models.
The definition of simultaneous confidence regions (SCRs) follows
Sommerfeld et al. (2018) <doi:10.1080/01621459.2017.1341838>. Methods for
estimating inverse regions, SCRs, and the nonparametric bootstrap are
based on Ren et al. (2024) <doi:10.1093/jrsssc/qlae027>. Methods for
constructing SCBs are described in Crainiceanu et al. (2024)
<doi:10.1201/9781003278726> and Telschow et al. (2022)
<doi:10.1016/j.jspi.2021.05.008>.

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
