%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CaMeA
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Causal Meta-Analysis for Aggregated Data

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-metafor 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 

%description
A tool for causal meta-analysis. This package implements the aggregation
formulas and inference methods proposed in Berenfeld et al. (2025)
<doi:10.48550/arXiv.2505.20168>. Users can input aggregated data across
multiple studies and compute causally meaningful aggregated effects of
their choice (risk difference, risk ratio, odds ratio, etc) under
user-specified population weighting. The built-in function camea() allows
to obtain precise variance estimates for these effects and to compare the
latter to a classical meta-analysis aggregate, the random effect model, as
implemented in the 'metafor' package
<https://CRAN.R-project.org/package=metafor>.

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
