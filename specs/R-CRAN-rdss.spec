%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rdss
%global packver   1.0.14
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.14
Release:          1%{?dist}%{?buildtag}
Summary:          Companion Datasets and Functions for Research Design in the Social Sciences

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dataverse 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-estimatr 
BuildRequires:    R-CRAN-randomizr 
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dataverse 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-estimatr 
Requires:         R-CRAN-randomizr 

%description
Helper functions to accompany the Blair, Coppock, and Humphreys (2022)
"Research Design in the Social Sciences: Declaration, Diagnosis, and
Redesign" <https://book.declaredesign.org>. 'rdss' includes datasets,
helper functions, and plotting components to enable use and replication of
the book.

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
