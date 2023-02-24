%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  globaltrends
%global packver   0.0.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.13
Release:          1%{?dist}%{?buildtag}
Summary:          Download and Measure Global Trends Through Google Search Volumes

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast >= 8.12
BuildRequires:    R-stats >= 3.5.0
BuildRequires:    R-utils >= 3.5.0
BuildRequires:    R-CRAN-maps >= 3.4.0
BuildRequires:    R-CRAN-ggplot2 >= 3.3.2
BuildRequires:    R-CRAN-tibble >= 3.0.3
BuildRequires:    R-CRAN-RSQLite >= 2.2.0
BuildRequires:    R-CRAN-zoo >= 1.8.8
BuildRequires:    R-CRAN-lubridate >= 1.7.9
BuildRequires:    R-CRAN-gtrendsR >= 1.5.1
BuildRequires:    R-CRAN-dbplyr >= 1.4.4
BuildRequires:    R-CRAN-glue >= 1.4.2
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-DBI >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 1.0.2
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-forcats >= 0.5.0
BuildRequires:    R-CRAN-rlang >= 0.4.7
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-ineq >= 0.2.13
Requires:         R-CRAN-forecast >= 8.12
Requires:         R-stats >= 3.5.0
Requires:         R-utils >= 3.5.0
Requires:         R-CRAN-maps >= 3.4.0
Requires:         R-CRAN-ggplot2 >= 3.3.2
Requires:         R-CRAN-tibble >= 3.0.3
Requires:         R-CRAN-RSQLite >= 2.2.0
Requires:         R-CRAN-zoo >= 1.8.8
Requires:         R-CRAN-lubridate >= 1.7.9
Requires:         R-CRAN-gtrendsR >= 1.5.1
Requires:         R-CRAN-dbplyr >= 1.4.4
Requires:         R-CRAN-glue >= 1.4.2
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-DBI >= 1.1.0
Requires:         R-CRAN-dplyr >= 1.0.2
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-forcats >= 0.5.0
Requires:         R-CRAN-rlang >= 0.4.7
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-ineq >= 0.2.13

%description
Google offers public access to global search volumes from its search
engine through the Google Trends portal. The package downloads these
search volumes provided by Google Trends and uses them to measure and
analyze the distribution of search scores across countries or within
countries. The package allows researchers and analysts to use these search
scores to investigate global trends based on patterns within these scores.
This offers insights such as degree of internationalization of firms and
organizations or dissemination of political, social, or technological
trends across the globe or within single countries.  An outline of the
package's methodological foundations and potential applications is
available as a working paper:
<https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3969013>.

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
