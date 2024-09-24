%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EQUALSTATS
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Algorithm Driven Statistical Analysis for Researchers without Coding Skills

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-zip 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-pwr 
BuildRequires:    R-CRAN-ggcorrplot 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-ThresholdROC 
BuildRequires:    R-CRAN-ggsurvfit 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-mclogit 
BuildRequires:    R-CRAN-ordinal 
BuildRequires:    R-CRAN-coxme 
BuildRequires:    R-CRAN-MuMIn 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-zip 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-DescTools 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-pwr 
Requires:         R-CRAN-ggcorrplot 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-ThresholdROC 
Requires:         R-CRAN-ggsurvfit 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-mclogit 
Requires:         R-CRAN-ordinal 
Requires:         R-CRAN-coxme 
Requires:         R-CRAN-MuMIn 

%description
Support functions for R-based 'EQUAL-STATS' software which automatically
classifies the data and performs appropriate statistical tests.
'EQUAL-STATS' software is a shiny application with an user-friendly
interface to perform complex statistical analysis. Gurusamy,K
(2024)<doi:10.5281/zenodo.13354162>.

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
