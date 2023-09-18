%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ivDiag
%global packver   1.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation and Diagnostic Tools for Instrumental Variables Designs

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-lfe 
BuildRequires:    R-CRAN-fixest 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggfortify 
BuildRequires:    R-CRAN-wCorr 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-testthat 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-future 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-lfe 
Requires:         R-CRAN-fixest 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggfortify 
Requires:         R-CRAN-wCorr 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-testthat 

%description
Estimation and diagnostic tools for instrumental variables designs, which
implements the guidelines proposed in Lal et al. (2023)
<arXiv:2303.11399>, including bootstrapped confidence intervals, effective
F-statistic, Anderson-Rubin test, valid-t ratio test, and local-to-zero
tests.

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
