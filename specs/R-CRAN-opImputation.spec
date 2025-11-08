%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  opImputation
%global packver   0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Optimal Selection of Imputation Methods for Pain-Related Numerical Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Rfit 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-ABCanalysis 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-missForest 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-miceRanger 
BuildRequires:    R-CRAN-multiUS 
BuildRequires:    R-CRAN-Amelia 
BuildRequires:    R-CRAN-mi 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-DataVisualizations 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-twosamples 
BuildRequires:    R-CRAN-ggh4x 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-tools 
Requires:         R-parallel 
Requires:         R-CRAN-Rfit 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-ABCanalysis 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-missForest 
Requires:         R-utils 
Requires:         R-CRAN-mice 
Requires:         R-CRAN-miceRanger 
Requires:         R-CRAN-multiUS 
Requires:         R-CRAN-Amelia 
Requires:         R-CRAN-mi 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-DataVisualizations 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-twosamples 
Requires:         R-CRAN-ggh4x 
Requires:         R-CRAN-ggrepel 
Requires:         R-tools 

%description
A model-agnostic framework for selecting dataset-specific imputation
methods for missing values in numerical data related to pain. Lotsch J,
Ultsch A (2025) "A model-agnostic framework for dataset-specific selection
of missing value imputation methods in pain-related numerical data"
Canadian Journal of Pain (in minor revision).

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
