%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  StatTeacherAssistant
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          An App that Assists Intro Statistics Instructors with Data Sets

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.5.0
Requires:         R-core >= 4.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.10.4
BuildRequires:    R-CRAN-ggplot2 >= 3.5.2
BuildRequires:    R-CRAN-shinyalert >= 3.1.0
BuildRequires:    R-CRAN-shinyjs >= 2.1.0
BuildRequires:    R-CRAN-stringi >= 1.8.7
BuildRequires:    R-CRAN-stringr >= 1.5.1
BuildRequires:    R-CRAN-tidyr >= 1.3.1
BuildRequires:    R-CRAN-rio >= 1.2.3
BuildRequires:    R-CRAN-extraDistr >= 1.10.0
BuildRequires:    R-CRAN-shiny >= 1.10.0
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-DescTools >= 0.99.60
BuildRequires:    R-CRAN-shinyBS >= 0.61.1
BuildRequires:    R-CRAN-sortable >= 0.5.0
BuildRequires:    R-CRAN-DT >= 0.33
BuildRequires:    R-CRAN-rhandsontable >= 0.3.8
BuildRequires:    R-CRAN-rmatio >= 0.19.0
Requires:         R-CRAN-plotly >= 4.10.4
Requires:         R-CRAN-ggplot2 >= 3.5.2
Requires:         R-CRAN-shinyalert >= 3.1.0
Requires:         R-CRAN-shinyjs >= 2.1.0
Requires:         R-CRAN-stringi >= 1.8.7
Requires:         R-CRAN-stringr >= 1.5.1
Requires:         R-CRAN-tidyr >= 1.3.1
Requires:         R-CRAN-rio >= 1.2.3
Requires:         R-CRAN-extraDistr >= 1.10.0
Requires:         R-CRAN-shiny >= 1.10.0
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-DescTools >= 0.99.60
Requires:         R-CRAN-shinyBS >= 0.61.1
Requires:         R-CRAN-sortable >= 0.5.0
Requires:         R-CRAN-DT >= 0.33
Requires:         R-CRAN-rhandsontable >= 0.3.8
Requires:         R-CRAN-rmatio >= 0.19.0

%description
Includes an interactive application designed to support educators in
wide-ranging disciplines, with a particular focus on those teaching
introductory statistical methods (descriptive and/or inferential) for data
analysis. Users are able to randomly generate data, make new versions of
existing data through common adjustments (e.g., add random normal noise
and perform transformations), and check the suitability of the resulting
data for statistical analyses.

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
