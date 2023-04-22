%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CopulaInference
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation and Goodness-of-Fit of Copula-Based Models with Arbitrary Distributions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rvinecopulib 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 
Requires:         R-CRAN-foreach 
Requires:         R-stats 
Requires:         R-CRAN-rvinecopulib 
Requires:         R-CRAN-Matrix 

%description
Estimation and goodness-of-fit functions for copula-based models of
bivariate data with arbitrary distributions (discrete, continuous, mixture
of both types). The copula families considered here are the Gaussian,
Student, Clayton, Frank, Gumbel, Joe, Plackett, BB1, BB6, BB7,BB8,
together with the following non-central squared copula families in Nasri
(2020) <doi:10.1016/j.spl.2020.108704>: ncs-gaussian, ncs-clayton,
ncs-gumbel, ncs-frank, ncs-joe, and ncs-plackett. For theoretical details,
see, e.g., Nasri and Remillard (2023) <arXiv:2301.13408>.

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
