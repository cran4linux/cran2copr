%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  wizaRdry
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Magical Framework for Collaborative & Reproducible Data Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-beepr 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-config 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-mongolite 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-qualtRics 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-REDCapR 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-lubridate 
Requires:         R-CRAN-beepr 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-config 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-mongolite 
Requires:         R-parallel 
Requires:         R-CRAN-qualtRics 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-REDCapR 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-testthat 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-lubridate 

%description
A comprehensive data analysis framework for NIH-funded research that
streamlines workflows for both data cleaning and preparing NIH Data
Archive ('NDA') submission templates. Provides unified access to multiple
data sources ('REDCap', 'MongoDB', 'Qualtrics') through interfaces to
their APIs, with specialized functions for data cleaning, filtering,
merging, and parsing. Features automatic validation, field harmonization,
and memory-aware processing to enhance reproducibility in multi-site
collaborative research as described in Mittal et al. (2021)
<doi:10.20900/jpbs.20210011>.

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
