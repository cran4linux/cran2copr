%global __brp_check_rpaths %{nil}
%global packname  skater
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Utilities for SNP-Based Kinship Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-kinship2 
BuildRequires:    R-CRAN-corrr 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-kinship2 
Requires:         R-CRAN-corrr 
Requires:         R-grDevices 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-rlang 

%description
Utilities for single nucleotide polymorphism (SNP) based kinship analysis
testing and evaluation. The 'skater' package contains functions for
importing, parsing, and analyzing pedigree data, performing relationship
degree inference, benchmarking relationship degree classification, and
summarizing identity by descent (IBD) segment data. Package functions and
methods are described in Turner et al. (2021) "skater: An R package for
SNP-based Kinship Analysis, Testing, and Evaluation"
<doi:10.1101/2021.07.21.453083>.

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
