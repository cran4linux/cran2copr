%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AICcPermanova
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Model Selection of PERMANOVA Models Using AICc

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-vegan 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-car 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-future 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-vegan 

%description
Provides tools for model selection and model averaging of PerMANOVA models
using Akaike Information Criterion corrected for small sample sizes (AICc)
and Information Theoretic criteria principles. The package is built around
the PERMANOVA analysis from the 'vegan' package and provides a streamlined
workflow for generating and comparing models, obtaining model weights, and
summarizing results using model averaging approaches.  The methods
implemented in this package are based on the practical information-
theoretic approach described by Burnham, K. P. and Anderson, D. R. (2002)
(<doi:10.1007/b97636>).

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
