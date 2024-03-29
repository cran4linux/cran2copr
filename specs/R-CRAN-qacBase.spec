%global __brp_check_rpaths %{nil}
%global packname  qacBase
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Functions to Facilitate Exploratory Data Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggcorrplot 
BuildRequires:    R-CRAN-multcompView 
BuildRequires:    R-CRAN-PMCMRplus 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-ggExtra 
BuildRequires:    R-CRAN-patchwork 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggcorrplot 
Requires:         R-CRAN-multcompView 
Requires:         R-CRAN-PMCMRplus 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-ggExtra 
Requires:         R-CRAN-patchwork 

%description
Functions for descriptive statistics, data management, and data
visualization.

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
