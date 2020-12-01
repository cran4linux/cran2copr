%global packname  Directional
%global packver   4.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.5
Release:          1%{?dist}%{?buildtag}
Summary:          A Collection of R Functions for Directional Data Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-bigstatsr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-Rfast2 
BuildRequires:    R-CRAN-rgl 
Requires:         R-CRAN-bigstatsr 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-Rfast2 
Requires:         R-CRAN-rgl 

%description
A collection of functions for directional data (including massive, with
millions of observations, data) analysis. Hypothesis testing, discriminant
and regression analysis, MLE of distributions and more are included. The
standard textbook for such data is the "Directional Statistics" by Mardia,
K. V. and Jupp, P. E. (2000). Other references include a) Phillip J.
Paine, Simon P. Preston Michail Tsagris and Andrew T. A. Wood (2018). An
elliptically symmetric angular Gaussian distribution. Statistics and
Computing 28(3): 689-697. <doi:10.1007/s11222-017-9756-4>. b) Tsagris M.
and Alenazi A. (2019). Comparison of discriminant analysis methods on the
sphere. Communications in Statistics: Case Studies, Data Analysis and
Applications 5(4):467--491. <doi:10.1080/23737484.2019.1684854>. c) P. J.
Paine, S. P. Preston, M. Tsagris and Andrew T. A. Wood (2020). Spherical
regression models with general covariates and anisotropic errors.
Statistics and Computing 30(1): 153--165.
<doi:10.1007/s11222-019-09872-2>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
