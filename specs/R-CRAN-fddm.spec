%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fddm
%global packver   1.0-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Implementation of the Diffusion Decision Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 1.0.1
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-Formula 

%description
Provides the probability density function (PDF), cumulative distribution
function (CDF), the first-order and second-order partial derivatives of
the PDF, and a fitting function for the diffusion decision model (DDM;
e.g., Ratcliff & McKoon, 2008, <doi:10.1162/neco.2008.12-06-420>) with
across-trial variability in the drift rate. Because the PDF, its partial
derivatives, and the CDF of the DDM both contain an infinite sum, they
need to be approximated. 'fddm' implements all published approximations
(Navarro & Fuss, 2009, <doi:10.1016/j.jmp.2009.02.003>; Gondan, Blurton, &
Kesselmeier, 2014, <doi:10.1016/j.jmp.2014.05.002>; Blurton, Kesselmeier,
& Gondan, 2017, <doi:10.1016/j.jmp.2016.11.003>; Hartmann & Klauer, 2021,
<doi:10.1016/j.jmp.2021.102550>) plus new approximations. All
approximations are implemented purely in 'C++' providing faster speed than
existing packages.

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
