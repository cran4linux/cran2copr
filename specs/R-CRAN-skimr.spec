%global packname  skimr
%global packver   2.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Compact and Flexible Summaries of Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 2.0.0
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-knitr >= 1.2
BuildRequires:    R-CRAN-stringr >= 1.1
BuildRequires:    R-CRAN-tidyselect >= 1.0.0
BuildRequires:    R-CRAN-tidyr >= 1.0
BuildRequires:    R-CRAN-dplyr >= 0.8.0
BuildRequires:    R-CRAN-rlang >= 0.3.1
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-repr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-tibble >= 2.0.0
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-knitr >= 1.2
Requires:         R-CRAN-stringr >= 1.1
Requires:         R-CRAN-tidyselect >= 1.0.0
Requires:         R-CRAN-tidyr >= 1.0
Requires:         R-CRAN-dplyr >= 0.8.0
Requires:         R-CRAN-rlang >= 0.3.1
Requires:         R-CRAN-cli 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-repr 
Requires:         R-stats 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-withr 

%description
A simple to use summary function that can be used with pipes and displays
nicely in the console. The default summary statistics may be modified by
the user as can the default formatting.  Support for data frames and
vectors is included, and users can implement their own skim methods for
specific object types as described in a vignette. Default summaries
include support for inline spark graphs. Instructions for managing these
on specific operating systems are given in the "Using skimr" vignette and
the README.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
