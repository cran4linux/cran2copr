%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  funcharts
%global packver   1.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          Functional Control Charts

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-roahd 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-fda.usc 
BuildRequires:    R-CRAN-rrcov 
BuildRequires:    R-CRAN-rofanova 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-scam 
BuildRequires:    R-CRAN-spatstat.univar 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 
Requires:         R-parallel 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-roahd 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-fda.usc 
Requires:         R-CRAN-rrcov 
Requires:         R-CRAN-rofanova 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-scam 
Requires:         R-CRAN-spatstat.univar 
Requires:         R-methods 

%description
Provides functional control charts for statistical process monitoring of
functional data, using the methods of Capezza et al. (2020)
<doi:10.1002/asmb.2507>, Centofanti et al. (2021)
<doi:10.1080/00401706.2020.1753581>, Capezza et al. (2024)
<doi:10.1080/00401706.2024.2327346>, Capezza et al. (2024)
<doi:10.1080/00224065.2024.2383674>, Centofanti et al. (2022)
<doi:10.48550/arXiv.2205.06256>. The package is thoroughly illustrated in
the paper of Capezza et al (2023) <doi:10.1080/00224065.2023.2219012>.

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
