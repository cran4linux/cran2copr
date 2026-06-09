%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Iscores
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Proper Scoring Rules for Missing Value Imputation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-energy 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-pbmcapply 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-scoringRules 
BuildRequires:    R-stats 
Requires:         R-CRAN-energy 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-pbmcapply 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-scoringRules 
Requires:         R-stats 

%description
Provides tools for evaluating and ranking missing value imputation methods
using proper scoring rules. Implements the Energy-I-Score and the
DR-I-Score for the assessment of deterministic, stochastic and multiple
imputation methods for numerical and mixed datasets, following Näf et al.
(2022) <doi:10.48550/arXiv.2106.03742> and Näf et al. (2025)
<doi:10.48550/arXiv.2507.11297>.

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
