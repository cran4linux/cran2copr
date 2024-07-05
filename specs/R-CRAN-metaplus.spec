%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  metaplus
%global packver   1.0-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Meta-Analysis and Meta-Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bbmle 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-fastGHQuad 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doRNG 
Requires:         R-CRAN-bbmle 
Requires:         R-CRAN-metafor 
Requires:         R-CRAN-boot 
Requires:         R-methods 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-MASS 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-fastGHQuad 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-Rfast 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doRNG 

%description
Performs meta-analysis and meta-regression using standard and robust
methods with confidence intervals based on the profile likelihood. Robust
methods are based on alternative distributions for the random effect,
either the t-distribution (Lee and Thompson, 2008 <doi:10.1002/sim.2897>
or Baker and Jackson, 2008 <doi:10.1007/s10729-007-9041-8>) or mixtures of
normals (Beath, 2014 <doi:10.1002/jrsm.1114>).

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
