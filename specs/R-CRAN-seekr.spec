%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  seekr
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Search, Inspect, and Replace Text Across Files

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.1
BuildRequires:    R-CRAN-rlang >= 1.1.1
BuildRequires:    R-CRAN-vctrs >= 0.6.3
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mime 
BuildRequires:    R-CRAN-pillar 
BuildRequires:    R-CRAN-processx 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
Requires:         R-CRAN-cli >= 3.6.1
Requires:         R-CRAN-rlang >= 1.1.1
Requires:         R-CRAN-vctrs >= 0.6.3
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-glue 
Requires:         R-methods 
Requires:         R-CRAN-mime 
Requires:         R-CRAN-pillar 
Requires:         R-CRAN-processx 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-utils 

%description
An inspectable and composable workflow for search-and-replace in text
files. Files can be listed, filtered, and searched separately, with
inspectable exclusions showing what was excluded and why. Matches are
represented as structured vectors that can be printed with context,
summarized, and filtered. Replacements can be defined at search time or
set and updated after the search. Only matches present in the vector are
modified when files are written. Backup and restore helpers are provided
for file workflows. Text that has already been read can also be searched
and updated directly, giving users control over input, output, and
encoding when needed.

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
