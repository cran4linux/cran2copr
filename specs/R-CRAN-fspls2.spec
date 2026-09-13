%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fspls2
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Package to Find Minimal Transcriptional Signatures

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-binom 
BuildRequires:    R-CRAN-confintr 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-binom 
Requires:         R-CRAN-confintr 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-RSQLite 
Requires:         R-methods 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-data.table 

%description
Identifies minimal biomarker signatures for predicting phenotypes from
multiomic data. Integrates multiple omics layers, supports internal
cross-validation. Supports missing values in predictors and outcomes.
Enables model based imputation of uncertain values. Supports continuous,
binary, multi-class and ordinal outcomes.

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
