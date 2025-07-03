%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Directional
%global packver   7.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          7.2
Release:          1%{?dist}%{?buildtag}
Summary:          A Collection of Functions for Directional Data Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-bigstatsr 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-Rfast2 
BuildRequires:    R-CRAN-Rnanoflann 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-rnaturalearth 
BuildRequires:    R-CRAN-sf 
Requires:         R-CRAN-bigstatsr 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-CRAN-magrittr 
Requires:         R-parallel 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-Rfast2 
Requires:         R-CRAN-Rnanoflann 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-rnaturalearth 
Requires:         R-CRAN-sf 

%description
A collection of functions for directional data (including massive data,
with millions of observations) analysis. Hypothesis testing, discriminant
and regression analysis, MLE of distributions and more are included. The
standard textbook for such data is the "Directional Statistics" by Mardia,
K. V. and Jupp, P. E. (2000). Other references include: a) Paine J.P.,
Preston S.P., Tsagris M. and Wood A.T.A. (2018). "An elliptically
symmetric angular Gaussian distribution". Statistics and Computing 28(3):
689-697. <doi:10.1007/s11222-017-9756-4>. b) Tsagris M. and Alenazi A.
(2019). "Comparison of discriminant analysis methods on the sphere".
Communications in Statistics: Case Studies, Data Analysis and Applications
5(4):467--491. <doi:10.1080/23737484.2019.1684854>. c) Paine J.P., Preston
S.P., Tsagris M. and Wood A.T.A. (2020). "Spherical regression models with
general covariates and anisotropic errors". Statistics and Computing
30(1): 153--165. <doi:10.1007/s11222-019-09872-2>. d) Tsagris M. and
Alenazi A. (2024). "An investigation of hypothesis testing procedures for
circular and spherical mean vectors". Communications in
Statistics-Simulation and Computation, 53(3): 1387--1408.
<doi:10.1080/03610918.2022.2045499>. e) Yu Z. and Huang X. (2024). A new
parameterization for elliptically symmetric angular Gaussian distributions
of arbitrary dimension. Electronic Journal of Statistics, 18(1): 301--334.
<doi:10.1214/23-EJS2210>. f) Tsagris M. and Alzeley O. (2024). "Circular
and spherical projected Cauchy distributions: A Novel Framework for
Circular and Directional Data Modeling". Australian & New Zealand Journal
of Statistics (Accepted for publication). <doi:10.1111/anzs.12434>. g)
Tsagris M., Papastamoulis P. and Kato S. (2024). "Directional data
analysis: spherical Cauchy or Poisson kernel-based distribution".
Statistics and Computing (Accepted for publication).
<doi:10.48550/arXiv.2409.03292>.

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
