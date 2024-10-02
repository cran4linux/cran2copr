%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GEInter
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Gene-Environment Interaction Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-pcaPP 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-MASS 
Requires:         R-splines 
Requires:         R-CRAN-pcaPP 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-graphics 

%description
Description: For the risk, progression, and response to treatment of many
complex diseases, it has been increasingly recognized that
gene-environment interactions play important roles beyond the main genetic
and environmental effects. In practical interaction analyses, outliers in
response variables and covariates are not uncommon. In addition,
missingness in environmental factors is routinely encountered in
epidemiological studies. The developed package consists of five robust
approaches to address the outliers problems, among which two approaches
can also accommodate missingness in environmental factors. Both continuous
and right censored responses are considered. The proposed approaches are
based on penalization and sparse boosting techniques for identifying
important interactions, which are realized using efficient algorithms.
Beyond the gene-environment analysis, the developed package can also be
adopted to conduct analysis on interactions between other types of
low-dimensional and high-dimensional data. (Mengyun Wu et al (2017),
<doi:10.1080/00949655.2018.1523411>; Mengyun Wu et al (2017),
<doi:10.1002/gepi.22055>; Yaqing Xu et al (2018),
<doi:10.1080/00949655.2018.1523411>; Yaqing Xu et al (2019),
<doi:10.1016/j.ygeno.2018.07.006>; Mengyun Wu et al (2021),
<doi:10.1093/bioinformatics/btab318>).

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
