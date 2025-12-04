%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hdcuremodels
%global packver   0.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          High-Dimensional Cure Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-flexsurv 
BuildRequires:    R-CRAN-flexsurvcure 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-knockoff 
BuildRequires:    R-CRAN-mvnfast 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-flexsurv 
Requires:         R-CRAN-flexsurvcure 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-knockoff 
Requires:         R-CRAN-mvnfast 
Requires:         R-parallel 
Requires:         R-CRAN-plyr 
Requires:         R-methods 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-withr 

%description
Provides functions for fitting various penalized parametric and
semi-parametric mixture cure models with different penalty functions,
testing for a significant cure fraction, and testing for sufficient
follow-up as described in Fu et al (2022)<doi:10.1002/sim.9513> and Archer
et al (2024)<doi:10.1186/s13045-024-01553-6>. False discovery rate
controlled variable selection is provided using model-X knock-offs.

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
