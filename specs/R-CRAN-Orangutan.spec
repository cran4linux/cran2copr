%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Orangutan
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Automated Analysis of Phenotypic Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-adegenet 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-dunn.test 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-multcompView 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-adegenet 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-dunn.test 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-multcompView 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-withr 

%description
Provides functions to analyze and visualize meristic and mensural
phenotypic data in a comparative framework. The package implements an
automated pipeline that summarizes traits, identifies diagnostic variables
among groups, performs multivariate and univariate statistical analyses,
and produces publication-ready graphics. An earlier implementation
(v1.0.0) is described in Torres (2025) <doi:10.64898/2025.12.18.695244>.

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
