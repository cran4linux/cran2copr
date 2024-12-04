%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tibbletime
%global packver   0.1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.9
Release:          1%{?dist}%{?buildtag}
Summary:          Time Aware Tibbles

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-tibble >= 3.1.8
BuildRequires:    R-CRAN-lubridate >= 1.9.1
BuildRequires:    R-CRAN-zoo >= 1.8.11
BuildRequires:    R-CRAN-pillar >= 1.8.1
BuildRequires:    R-CRAN-glue >= 1.6.2
BuildRequires:    R-CRAN-hms >= 1.1.2
BuildRequires:    R-CRAN-Rcpp >= 1.0.9
BuildRequires:    R-CRAN-rlang >= 1.0.6
BuildRequires:    R-CRAN-lifecycle >= 1.0.3
BuildRequires:    R-CRAN-dplyr >= 1.0.10
BuildRequires:    R-CRAN-vctrs >= 0.5.0
BuildRequires:    R-CRAN-purrr >= 0.3.5
BuildRequires:    R-CRAN-assertthat >= 0.2.1
Requires:         R-CRAN-tibble >= 3.1.8
Requires:         R-CRAN-lubridate >= 1.9.1
Requires:         R-CRAN-zoo >= 1.8.11
Requires:         R-CRAN-pillar >= 1.8.1
Requires:         R-CRAN-glue >= 1.6.2
Requires:         R-CRAN-hms >= 1.1.2
Requires:         R-CRAN-Rcpp >= 1.0.9
Requires:         R-CRAN-rlang >= 1.0.6
Requires:         R-CRAN-lifecycle >= 1.0.3
Requires:         R-CRAN-dplyr >= 1.0.10
Requires:         R-CRAN-vctrs >= 0.5.0
Requires:         R-CRAN-purrr >= 0.3.5
Requires:         R-CRAN-assertthat >= 0.2.1

%description
Built on top of the 'tibble' package, 'tibbletime' is an extension that
allows for the creation of time aware tibbles. Some immediate advantages
of this include: the ability to perform time-based subsetting on tibbles,
quickly summarising and aggregating results by time periods, and creating
columns that can be used as 'dplyr' time-based groups.

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
