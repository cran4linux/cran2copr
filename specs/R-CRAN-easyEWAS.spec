%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  easyEWAS
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Perform and Visualize EWAS Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-CMplot 
BuildRequires:    R-CRAN-ddpcr 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-lmerTest 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-tictoc 
BuildRequires:    R-CRAN-vroom 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-lubridate 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-CMplot 
Requires:         R-CRAN-ddpcr 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-lmerTest 
Requires:         R-CRAN-magrittr 
Requires:         R-parallel 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-tictoc 
Requires:         R-CRAN-vroom 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-lubridate 

%description
Tools for conducting epigenome-wide association studies (EWAS) and
visualizing results. Users provide sample metadata and methylation
matrices to run EWAS with linear models, linear mixed-effects models, or
Cox models. The package supports downstream visualization, bootstrap
validation, enrichment analysis, batch effect correction, and
differentially methylated region (DMR) analysis with optional parallel
computing. Methods are described in Wang et al. (2025)
<doi:10.1093/bioadv/vbaf026>, Johnson et al. (2007)
<doi:10.1093/biostatistics/kxj037>, and Peters et al. (2015)
<doi:10.1186/1756-8935-8-6>.

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
