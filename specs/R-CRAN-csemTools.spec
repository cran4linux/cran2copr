%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  csemTools
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Conditional Standard Error of Measurement Tools for Test Scores

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-patchwork 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-patchwork 

%description
Compute and compare conditional standard errors of measurement (CSEM)
across score distributions using methods from classical test theory.
Includes approaches for smoothing, bootstrapped CSEM, standardized CSEM,
CSEM for scale scores, and assessment of properties of split-half scores.
Also supports comparison with global standard errors derived from
reliability coefficients and graphical visualization of CSEM curves and
relative precision across observed score ranges. Some of these implemented
methods are based on work by Lord (1955)
<doi:10.1002/j.2333-8504.1955.tb00054.x>, Feldt and Qualls (1996)
<doi:10.1111/j.1745-3984.1996.tb00486.x>, McNeish and Dumas (2025)
<doi:10.3758/s13428-025-02611-8>.

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
