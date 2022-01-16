%global __brp_check_rpaths %{nil}
%global packname  statsExpressions
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tidy Dataframes and Expressions with Statistical Details

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-WRS2 >= 1.1.3
BuildRequires:    R-CRAN-BayesFactor >= 0.9.12.4.3
BuildRequires:    R-CRAN-performance >= 0.8.0
BuildRequires:    R-CRAN-correlation >= 0.7.1
BuildRequires:    R-CRAN-effectsize >= 0.6.0
BuildRequires:    R-CRAN-datawizard >= 0.2.2
BuildRequires:    R-CRAN-parameters >= 0.16.0
BuildRequires:    R-CRAN-insight >= 0.15.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-zeallot 
Requires:         R-CRAN-WRS2 >= 1.1.3
Requires:         R-CRAN-BayesFactor >= 0.9.12.4.3
Requires:         R-CRAN-performance >= 0.8.0
Requires:         R-CRAN-correlation >= 0.7.1
Requires:         R-CRAN-effectsize >= 0.6.0
Requires:         R-CRAN-datawizard >= 0.2.2
Requires:         R-CRAN-parameters >= 0.16.0
Requires:         R-CRAN-insight >= 0.15.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-zeallot 

%description
Utilities for producing dataframes with rich details for the most common
types of statistical approaches and tests: parametric, nonparametric,
robust, and Bayesian t-test, one-way ANOVA, correlation analyses,
contingency table analyses, and meta-analyses. The functions are
pipe-friendly and provide a consistent syntax to work with tidy data.
These dataframes additionally contain expressions with statistical
details, and can be used in graphing packages. This package also forms the
statistical processing backend for 'ggstatsplot'.

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
