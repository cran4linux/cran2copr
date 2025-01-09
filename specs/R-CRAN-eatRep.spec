%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  eatRep
%global packver   0.15.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.15.0
Release:          1%{?dist}%{?buildtag}
Summary:          Educational Assessment Tools for Replication Methods

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-survey >= 4.1.1
BuildRequires:    R-CRAN-mice >= 2.46
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-eatTools >= 0.7.8
BuildRequires:    R-CRAN-lavaan >= 0.6.7
BuildRequires:    R-CRAN-eatGADS >= 0.20.0
BuildRequires:    R-CRAN-BIFIEsurvey 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-fmsb 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-miceadds 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-EffectLiteR 
BuildRequires:    R-CRAN-estimatr 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-future 
Requires:         R-CRAN-survey >= 4.1.1
Requires:         R-CRAN-mice >= 2.46
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-eatTools >= 0.7.8
Requires:         R-CRAN-lavaan >= 0.6.7
Requires:         R-CRAN-eatGADS >= 0.20.0
Requires:         R-CRAN-BIFIEsurvey 
Requires:         R-CRAN-progress 
Requires:         R-parallel 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-fmsb 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-car 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-miceadds 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-EffectLiteR 
Requires:         R-CRAN-estimatr 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-lme4 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-future 

%description
Replication methods to compute some basic statistic operations (means,
standard deviations, frequency tables, percentiles, mean comparisons using
weighted effect coding, generalized linear models, and linear multilevel
models) in complex survey designs comprising multiple imputed or nested
imputed variables and/or a clustered sampling structure which both deserve
special procedures at least in estimating standard errors. See the package
documentation for a more detailed description along with references.

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
