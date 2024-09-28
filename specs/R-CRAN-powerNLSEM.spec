%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  powerNLSEM
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Simulation-Based Power Estimation (MSPE) for Nonlinear SEM

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-lavaan >= 0.6.16
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-lavaan >= 0.6.16
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-stringr 

%description
Model-implied simulation-based power estimation (MSPE) for nonlinear (and
linear) SEM, path analysis and regression analysis. A theoretical
framework is used to approximate the relation between power and sample
size for given type I error rates and effect sizes. The package offers an
adaptive search algorithm to find the optimal N for given effect sizes and
type I error rates. Plots can be used to visualize the power relation to N
for different parameters of interest (POI). Theoretical justifications are
given in Irmer et al. (2024a) <doi:10.31219/osf.io/pe5bj> and detailed
description are given in Irmer et al. (2024b)
<doi:10.3758/s13428-024-02476-3>.

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
