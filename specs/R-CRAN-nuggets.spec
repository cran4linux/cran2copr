%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nuggets
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Extensible Framework for Data Pattern Exploration

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-classInt 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-fastmatch 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-BH 
BuildRequires:    R-CRAN-RcppThread 
BuildRequires:    R-CRAN-testthat 
Requires:         R-CRAN-classInt 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-fastmatch 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-lifecycle 
Requires:         R-methods 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-utils 

%description
A framework for systematic exploration of association rules (Agrawal et
al., 1994, <https://www.vldb.org/conf/1994/P487.PDF>), contrast patterns
(Chen, 2022, <doi:10.48550/arXiv.2209.13556>), emerging patterns (Dong et
al., 1999, <doi:10.1145/312129.312191>), subgroup discovery (Atzmueller,
2015, <doi:10.1002/widm.1144>), and conditional correlations (Hájek, 1978,
<doi:10.1007/978-3-642-66943-9>). User-defined functions may also be
supplied to guide custom pattern searches. Supports both crisp (Boolean)
and fuzzy data. Generates candidate conditions expressed as elementary
conjunctions, evaluates them on a dataset, and inspects the induced
sub-data for statistical, logical, or structural properties such as
associations, correlations, or contrasts. Includes methods for
visualization of logical structures and supports interactive exploration
through integrated Shiny applications.

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
