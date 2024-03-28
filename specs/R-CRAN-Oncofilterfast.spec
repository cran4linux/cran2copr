%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Oncofilterfast
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Aids in the Analysis of Genes Influencing Cancer Survival

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-survminer 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-survminer 

%description
Aids in the analysis of genes influencing cancer survival by including a
principal function, calculator(), which calculates the P-value for each
provided gene under the optimal cutoff in cancer survival studies.
Grounded in methodologies from significant works, this package references
Therneau's 'survival' package (Therneau, 2024;
<https://CRAN.R-project.org/package=survival>) and the survival analysis
extensions by Therneau and Grambsch (2000, ISBN 0-387-98784-3). It also
integrates the 'survminer' package by Kassambara et al. (2021;
<https://CRAN.R-project.org/package=survminer>), enhancing survival curve
visualizations with 'ggplot2'.

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
