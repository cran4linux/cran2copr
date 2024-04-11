%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rtpcr
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          qPCR Data Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-agricolae 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-emmeans 
Requires:         R-CRAN-agricolae 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lme4 
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
Ganger et al. (2017) <doi:10.1186/s12859-017-1949-5>, covering both the
Livak and Pfaffl methods. Based on the experimental conditions, the
functions of the 'rtpcr' package use t-test (for experiments with a
two-level factor) or analysis of variance (for cases where more than two
levels or factors exist) to calculate the fold change or relative
expression. The functions also provide standard deviations and confidence
limits for means and apply statistical mean comparisons. To facilitate
using 'rtpcr', different datasets have been employed in the examples and
the outputs are explained. An outstanding feature of 'rtpcr' package is
providing publication-ready bar plots with various controlling arguments
for experiments with up to three different factors. The 'rtpcr' package is
user-friendly and easy to work with and provides an applicable resource
for analyzing real-time PCR data.

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
