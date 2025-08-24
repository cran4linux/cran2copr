%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pliman
%global packver   3.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Plant Image Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-exactextractr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mirai 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-exactextractr 
Requires:         R-methods 
Requires:         R-CRAN-mirai 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-terra 

%description
Tools for both single and batch image manipulation and analysis (Olivoto,
2022 <doi:10.1111/2041-210X.13803>) and phytopathometry (Olivoto et al.,
2022 <doi:10.1007/S40858-021-00487-5>). The tools can be used for the
quantification of leaf area, object counting, extraction of image indexes,
shape measurement, object landmark identification, and Elliptical Fourier
Analysis of object outlines (Claude (2008)
<doi:10.1007/978-0-387-77789-4>). The package also provides a
comprehensive pipeline for generating shapefiles with complex layouts and
supports high-throughput phenotyping of RGB, multispectral, and
hyperspectral orthomosaics. This functionality facilitates field
phenotyping using UAV- or satellite-based imagery.

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
