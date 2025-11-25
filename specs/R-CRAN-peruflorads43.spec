%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  peruflorads43
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Check Threatened Plant Species Status Against Peru's Supreme Decree 043-2006-AG

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.1.0
BuildRequires:    R-CRAN-readr >= 2.1.0
BuildRequires:    R-CRAN-memoise >= 2.0.1
BuildRequires:    R-CRAN-stringr >= 1.5.0
BuildRequires:    R-CRAN-tidyr >= 1.3.0
BuildRequires:    R-CRAN-progress >= 1.2.2
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-purrr >= 1.0.0
BuildRequires:    R-CRAN-assertthat >= 0.2.1
BuildRequires:    R-CRAN-fuzzyjoin >= 0.1.6
Requires:         R-CRAN-tibble >= 3.1.0
Requires:         R-CRAN-readr >= 2.1.0
Requires:         R-CRAN-memoise >= 2.0.1
Requires:         R-CRAN-stringr >= 1.5.0
Requires:         R-CRAN-tidyr >= 1.3.0
Requires:         R-CRAN-progress >= 1.2.2
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-purrr >= 1.0.0
Requires:         R-CRAN-assertthat >= 0.2.1
Requires:         R-CRAN-fuzzyjoin >= 0.1.6

%description
Provides tools to match plant species names against the official
threatened species list of Peru (Supreme Decree 043-2006-AG, 2006).
Implements a hierarchical matching pipeline with exact, fuzzy, and suffix
matching algorithms to handle naming variations and taxonomic changes.
Supports both the original 2006 nomenclature and updated taxonomic names,
allowing users to check protection status regardless of nomenclatural
changes since the decree's publication. Threat categories follow
International Union for Conservation of Nature standards (Critically
Endangered, Endangered, Vulnerable, Near Threatened).

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
