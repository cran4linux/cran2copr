%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  COINr
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Composite Indicator Construction and Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-openxlsx >= 4.2.3
BuildRequires:    R-CRAN-ggplot2 >= 3.3.3
BuildRequires:    R-CRAN-readxl >= 1.3.1
BuildRequires:    R-CRAN-rlang >= 0.4.10
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-openxlsx >= 4.2.3
Requires:         R-CRAN-ggplot2 >= 3.3.3
Requires:         R-CRAN-readxl >= 1.3.1
Requires:         R-CRAN-rlang >= 0.4.10
Requires:         R-stats 
Requires:         R-utils 

%description
A comprehensive high-level package, for composite indicator construction
and analysis. It is a "development environment" for composite indicators
and scoreboards, which includes utilities for construction (indicator
selection, denomination, imputation, data treatment, normalisation,
weighting and aggregation) and analysis (multivariate analysis,
correlation plotting, short cuts for principal component analysis, global
sensitivity analysis, and more). A composite indicator is completely
encapsulated inside a single hierarchical list called a "coin". This
allows a fast and efficient work flow, as well as making quick copies,
testing methodological variations and making comparisons. It also includes
many plotting options, both statistical (scatter plots, distribution
plots) as well as for presenting results.

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
