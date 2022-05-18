%global __brp_check_rpaths %{nil}
%global packname  repoRter.nih
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          R Interface to the 'NIH RePORTER Project' API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.1.3
BuildRequires:    R-CRAN-janitor >= 2.1.0
BuildRequires:    R-CRAN-magrittr >= 2.0.1
BuildRequires:    R-CRAN-jsonlite >= 1.7.2
BuildRequires:    R-CRAN-lubridate >= 1.7.10
BuildRequires:    R-CRAN-httr >= 1.4.2
BuildRequires:    R-CRAN-crayon >= 1.4.1
BuildRequires:    R-CRAN-dplyr >= 1.0.7
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-assertthat >= 0.2.1
Requires:         R-CRAN-tibble >= 3.1.3
Requires:         R-CRAN-janitor >= 2.1.0
Requires:         R-CRAN-magrittr >= 2.0.1
Requires:         R-CRAN-jsonlite >= 1.7.2
Requires:         R-CRAN-lubridate >= 1.7.10
Requires:         R-CRAN-httr >= 1.4.2
Requires:         R-CRAN-crayon >= 1.4.1
Requires:         R-CRAN-dplyr >= 1.0.7
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-assertthat >= 0.2.1

%description
Methods to easily build requests in the non-standard JSON schema required
by the National Institute of Health (NIH)'s 'RePORTER Project API'
<https://api.reporter.nih.gov/#/Search/post_v2_projects_search>. Also
retrieve and process result sets as either a ragged or flattened 'tibble'.

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
