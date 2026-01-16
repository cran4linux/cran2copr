%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AdhereRViz
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Adherence to Medications

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-RSQLite >= 2.1
BuildRequires:    R-CRAN-data.table >= 1.9
BuildRequires:    R-CRAN-V8 >= 1.5
BuildRequires:    R-CRAN-knitr >= 1.20
BuildRequires:    R-CRAN-RMariaDB >= 1.0.5
BuildRequires:    R-CRAN-manipulate >= 1.0
BuildRequires:    R-CRAN-shiny >= 1.0
BuildRequires:    R-CRAN-shinyjs >= 1.0
BuildRequires:    R-CRAN-colourpicker >= 1.0
BuildRequires:    R-CRAN-DBI >= 1.0
BuildRequires:    R-CRAN-AdhereR >= 0.7.1
BuildRequires:    R-CRAN-shinyWidgets >= 0.4.4
BuildRequires:    R-CRAN-highlight >= 0.4
BuildRequires:    R-CRAN-clipr >= 0.4
BuildRequires:    R-CRAN-viridisLite >= 0.3
Requires:         R-CRAN-RSQLite >= 2.1
Requires:         R-CRAN-data.table >= 1.9
Requires:         R-CRAN-V8 >= 1.5
Requires:         R-CRAN-knitr >= 1.20
Requires:         R-CRAN-RMariaDB >= 1.0.5
Requires:         R-CRAN-manipulate >= 1.0
Requires:         R-CRAN-shiny >= 1.0
Requires:         R-CRAN-shinyjs >= 1.0
Requires:         R-CRAN-colourpicker >= 1.0
Requires:         R-CRAN-DBI >= 1.0
Requires:         R-CRAN-AdhereR >= 0.7.1
Requires:         R-CRAN-shinyWidgets >= 0.4.4
Requires:         R-CRAN-highlight >= 0.4
Requires:         R-CRAN-clipr >= 0.4
Requires:         R-CRAN-viridisLite >= 0.3

%description
Interactive graphical user interface (GUI) for the package 'AdhereR',
allowing the user to access different data sources, to explore the
patterns of medication use therein, and the computation of various
measures of adherence. It is implemented using Shiny and
HTML/CSS/JavaScript.

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
