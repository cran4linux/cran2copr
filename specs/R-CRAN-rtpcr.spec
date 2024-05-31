%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rtpcr
%global packver   1.0.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.9
Release:          1%{?dist}%{?buildtag}
Summary:          qPCR Data Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-multcompView 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lmerTest 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-emmeans 
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-multcompView 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lmerTest 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-grid 
Requires:         R-CRAN-emmeans 

%description
Various methods are employed for statistical analysis and graphical
presentation of real-time PCR (quantitative PCR or qPCR) data. 'rtpcr'
handles amplification efficiency calculation, statistical analysis and
graphical representation of real-time PCR data based on up to two
reference genes. By accounting for amplification efficiency values,
'rtpcr' was developed using a general calculation method described by
Ganger et al. (2017) <doi:10.1186/s12859-017-1949-5> and Taylor et al.
(2019) <doi:10.1016/j.tibtech.2018.12.002>, covering both the Livak and
Pfaffl methods. Based on the experimental conditions, the functions of the
'rtpcr' package use t-test (for experiments with a two-level factor),
analysis of variance (ANOVA), analysis of covariance (ANCOVA) or analysis
of repeated measure data to calculate the fold change (FC, Delta Delta Ct
method) or relative expression (RE, Delta Ct method). The functions
further provide standard errors and confidence intervals for means, apply
statistical mean comparisons and present significance. To facilitate
function application, different data sets were used as examples and the
outputs were explained. ‘rtpcr’ package also provides bar plots using
various controlling arguments. The 'rtpcr' package is user-friendly and
easy to work with and provides an applicable resource for analyzing
real-time PCR data.

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
