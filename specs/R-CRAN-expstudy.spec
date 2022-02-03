%global __brp_check_rpaths %{nil}
%global packname  expstudy
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Experience Study Tools for Analytics and Communications

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.1.6
BuildRequires:    R-CRAN-cli >= 3.1.0
BuildRequires:    R-CRAN-withr >= 2.4.3
BuildRequires:    R-CRAN-magrittr >= 2.0.1
BuildRequires:    R-CRAN-pillar >= 1.6.4
BuildRequires:    R-CRAN-glue >= 1.6.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-dtplyr >= 1.2.0
BuildRequires:    R-CRAN-data.table >= 1.14.2
BuildRequires:    R-CRAN-tidyr >= 1.1.4
BuildRequires:    R-CRAN-tidyselect >= 1.1.1
BuildRequires:    R-CRAN-dplyr >= 1.0.7
BuildRequires:    R-CRAN-lifecycle >= 1.0.1
BuildRequires:    R-CRAN-rlang >= 0.4.11
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-assertthat >= 0.2.1
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-tibble >= 3.1.6
Requires:         R-CRAN-cli >= 3.1.0
Requires:         R-CRAN-withr >= 2.4.3
Requires:         R-CRAN-magrittr >= 2.0.1
Requires:         R-CRAN-pillar >= 1.6.4
Requires:         R-CRAN-glue >= 1.6.0
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-dtplyr >= 1.2.0
Requires:         R-CRAN-data.table >= 1.14.2
Requires:         R-CRAN-tidyr >= 1.1.4
Requires:         R-CRAN-tidyselect >= 1.1.1
Requires:         R-CRAN-dplyr >= 1.0.7
Requires:         R-CRAN-lifecycle >= 1.0.1
Requires:         R-CRAN-rlang >= 0.4.11
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-assertthat >= 0.2.1
Requires:         R-CRAN-checkmate 
Requires:         R-methods 
Requires:         R-utils 

%description
Provides a data class of 'tbl_es' to help aid in the formation and
analyses of recurrent or novel experience studies. A 'tbl_es' has
attributes which identify the key variables used for calculating metrics
under an actuarial perspective. Common metrics (such as actual-to-expected
analysis) can be quickly generated in aggregate or according to different
qualitative factors. If multiple factors are of interest, grouped metrics
can be automatically computed for each factor individually as well as for
all possible combinations. All resulting output can then be formatted for
presentations or left unformatted for subsequent analyses. Ultimately,
this package aims to reduce time spent completing repetitive code
therefore increasing time for analysis and insight.

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
