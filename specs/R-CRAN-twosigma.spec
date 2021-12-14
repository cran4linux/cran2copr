%global __brp_check_rpaths %{nil}
%global packname  twosigma
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          DE Analysis for Single-Cell RNA-Sequencing Data

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-parallel >= 3.6.3
BuildRequires:    R-CRAN-pscl >= 1.5.5
BuildRequires:    R-CRAN-multcomp >= 1.4.13
BuildRequires:    R-CRAN-pbapply >= 1.4.0
BuildRequires:    R-CRAN-doParallel >= 1.0.15
BuildRequires:    R-CRAN-glmmTMB 
BuildRequires:    R-methods 
Requires:         R-parallel >= 3.6.3
Requires:         R-CRAN-pscl >= 1.5.5
Requires:         R-CRAN-multcomp >= 1.4.13
Requires:         R-CRAN-pbapply >= 1.4.0
Requires:         R-CRAN-doParallel >= 1.0.15
Requires:         R-CRAN-glmmTMB 
Requires:         R-methods 

%description
Implements the TWO-Component Single Cell Model-Based Association Method
(TWO-SIGMA) for gene-level differential expression (DE) analysis and
DE-based gene set testing of single-cell RNA-sequencing datasets. See Van
Buren et al. (2020) <doi:10.1002/gepi.22361> and Van Buren et al. (2021)
<doi:10.1101/2021.01.24.427979>.

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
