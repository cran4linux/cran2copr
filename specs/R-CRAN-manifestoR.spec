%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  manifestoR
%global packver   1.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.2
Release:          1%{?dist}%{?buildtag}
Summary:          Access and Process Data and Documents of the Manifesto Project

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 2.0.0
BuildRequires:    R-CRAN-readr >= 1.2.0
BuildRequires:    R-CRAN-httr >= 1.0.0
BuildRequires:    R-CRAN-tidyselect >= 1.0.0
BuildRequires:    R-CRAN-jsonlite >= 0.9.12
BuildRequires:    R-CRAN-dplyr >= 0.7.5
BuildRequires:    R-CRAN-tm >= 0.7.12
BuildRequires:    R-CRAN-functional >= 0.6
BuildRequires:    R-CRAN-purrr >= 0.2.4
BuildRequires:    R-CRAN-NLP >= 0.2.0
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-base64enc 
Requires:         R-CRAN-tibble >= 2.0.0
Requires:         R-CRAN-readr >= 1.2.0
Requires:         R-CRAN-httr >= 1.0.0
Requires:         R-CRAN-tidyselect >= 1.0.0
Requires:         R-CRAN-jsonlite >= 0.9.12
Requires:         R-CRAN-dplyr >= 0.7.5
Requires:         R-CRAN-tm >= 0.7.12
Requires:         R-CRAN-functional >= 0.6
Requires:         R-CRAN-purrr >= 0.2.4
Requires:         R-CRAN-NLP >= 0.2.0
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-base64enc 

%description
Provides access to coded election programmes from the Manifesto Corpus and
to the Manifesto Project's Main Dataset and routines to analyse this data.
The Manifesto Project <https://manifesto-project.wzb.eu> collects and
analyses election programmes across time and space to measure the
political preferences of parties. The Manifesto Corpus contains the
collected and annotated election programmes in the Corpus format of the
package 'tm' to enable easy use of text processing and text mining
functionality. Specific functions for scaling of coded political texts are
included.

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
