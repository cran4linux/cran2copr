%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  apc
%global packver   3.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Age-Period-Cohort Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-plm 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-AER 
BuildRequires:    R-CRAN-ISLR 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-plm 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-car 
Requires:         R-CRAN-AER 
Requires:         R-CRAN-ISLR 
Requires:         R-CRAN-ggplot2 

%description
Functions for age-period-cohort analysis. Aggregate data can be organised
in matrices indexed by age-cohort, age-period or cohort-period. The data
can include dose and response or just doses. The statistical model is a
generalized linear model (GLM) allowing for 3,2,1 or 0 of the
age-period-cohort factors. 2-sample analysis is possible. Mixed frequency
data are possible. Individual-level data should have a row for each
individual and columns for each of age, period, and cohort. The
statistical model for repeated cross-section is a generalized linear
model. The statistical model for panel data is ordinary least squares. The
canonical parametrisation of Kuang, Nielsen and Nielsen (2008)
<DOI:10.1093/biomet/asn026> is used. Thus, the analysis does not rely on
ad hoc identification.

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
