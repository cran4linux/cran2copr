%global __brp_check_rpaths %{nil}
%global packname  lmeresampler
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Bootstrap Methods for Nested Linear Mixed-Effects Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 0.8.0
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-nlmeU 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggdist 
BuildRequires:    R-CRAN-HLMdiag 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-dplyr >= 0.8.0
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-nlmeU 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggdist 
Requires:         R-CRAN-HLMdiag 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-forcats 
Requires:         R-stats 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tibble 

%description
Bootstrap routines for nested linear mixed effects models fit using either
'lme4' or 'nlme'. The provided 'bootstrap()' function implements the
parametric, residual, cases, random effect block (REB), and wild bootstrap
procedures. An overview of these procedures can be found in Van der Leeden
et al. (2008) <doi: 10.1007/978-0-387-73186-5_11>, Carpenter, Goldstein &
Rasbash (2003) <doi: 10.1111/1467-9876.00415>, and Chambers & Chandra
(2013) <doi: 10.1080/10618600.2012.681216>.

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
