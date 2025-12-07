%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  statsExpressions
%global packver   1.7.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.2
Release:          1%{?dist}%{?buildtag}
Summary:          Tidy Dataframes and Expressions with Statistical Details

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-withr >= 3.0.2
BuildRequires:    R-CRAN-rstantools >= 2.5.0
BuildRequires:    R-CRAN-magrittr >= 2.0.4
BuildRequires:    R-CRAN-PMCMRplus >= 1.9.12
BuildRequires:    R-CRAN-glue >= 1.8.0
BuildRequires:    R-CRAN-afex >= 1.5.0
BuildRequires:    R-CRAN-insight >= 1.4.3
BuildRequires:    R-CRAN-tidyr >= 1.3.1
BuildRequires:    R-CRAN-datawizard >= 1.3.0
BuildRequires:    R-CRAN-purrr >= 1.2.0
BuildRequires:    R-CRAN-WRS2 >= 1.1.7
BuildRequires:    R-CRAN-rlang >= 1.1.6
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-effectsize >= 1.0.1
BuildRequires:    R-CRAN-BayesFactor >= 0.9.12.4.7
BuildRequires:    R-CRAN-correlation >= 0.8.8
BuildRequires:    R-CRAN-parameters >= 0.28.3
BuildRequires:    R-CRAN-zeallot >= 0.2.0
BuildRequires:    R-CRAN-bayestestR >= 0.17.0
BuildRequires:    R-CRAN-performance >= 0.15.3
BuildRequires:    R-stats 
Requires:         R-CRAN-withr >= 3.0.2
Requires:         R-CRAN-rstantools >= 2.5.0
Requires:         R-CRAN-magrittr >= 2.0.4
Requires:         R-CRAN-PMCMRplus >= 1.9.12
Requires:         R-CRAN-glue >= 1.8.0
Requires:         R-CRAN-afex >= 1.5.0
Requires:         R-CRAN-insight >= 1.4.3
Requires:         R-CRAN-tidyr >= 1.3.1
Requires:         R-CRAN-datawizard >= 1.3.0
Requires:         R-CRAN-purrr >= 1.2.0
Requires:         R-CRAN-WRS2 >= 1.1.7
Requires:         R-CRAN-rlang >= 1.1.6
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-effectsize >= 1.0.1
Requires:         R-CRAN-BayesFactor >= 0.9.12.4.7
Requires:         R-CRAN-correlation >= 0.8.8
Requires:         R-CRAN-parameters >= 0.28.3
Requires:         R-CRAN-zeallot >= 0.2.0
Requires:         R-CRAN-bayestestR >= 0.17.0
Requires:         R-CRAN-performance >= 0.15.3
Requires:         R-stats 

%description
Utilities for producing dataframes with rich details for the most common
types of statistical approaches and tests: parametric, nonparametric,
robust, and Bayesian t-test, one-way ANOVA, correlation analyses,
contingency table analyses, and meta-analyses. The functions are
pipe-friendly and provide a consistent syntax to work with tidy data.
These dataframes additionally contain expressions with statistical
details, and can be used in graphing packages. This package also forms the
statistical processing backend for 'ggstatsplot'. References: Patil (2021)
<doi:10.21105/joss.03236>.

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
