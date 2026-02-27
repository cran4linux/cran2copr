%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MethScope
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Ultra-Fast Analysis of Sparse DNA Methylome via Recurrent Pattern Encoding

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-uwot 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-nnls 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-dplyr 
Requires:         R-utils 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-uwot 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-nnls 

%description
Methods for analyzing DNA methylation data via Most Recurrent Methylation
Patterns (MRMPs). Supports cell-type annotation, spatial deconvolution,
unsupervised clustering, and cancer cell-of-origin inference. Includes
C-backed summaries for YAME “.cg/.cm” files (overlap counts, log2 odds
ratios, beta/depth aggregation), an XGBoost classifier, NNLS
deconvolution, and plotting utilities. Scales to large spatial and
single-cell methylomes and is robust to extreme sparsity.

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
