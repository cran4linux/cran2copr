%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  shinyquiz
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Create Interactive Quizzes in 'shiny'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-methods >= 4.0.0
BuildRequires:    R-CRAN-cli >= 3.6.1
BuildRequires:    R-CRAN-shinyjs >= 2.1.0
BuildRequires:    R-CRAN-shiny >= 1.7.4
BuildRequires:    R-CRAN-stringi >= 1.7.12
BuildRequires:    R-CRAN-glue >= 1.6.2
BuildRequires:    R-CRAN-stringr >= 1.5.0
BuildRequires:    R-CRAN-scales >= 1.2.1
BuildRequires:    R-CRAN-purrr >= 1.0.1
BuildRequires:    R-CRAN-htmltools >= 0.5.5
BuildRequires:    R-CRAN-fontawesome >= 0.5.0
BuildRequires:    R-CRAN-reactable >= 0.4.4
Requires:         R-methods >= 4.0.0
Requires:         R-CRAN-cli >= 3.6.1
Requires:         R-CRAN-shinyjs >= 2.1.0
Requires:         R-CRAN-shiny >= 1.7.4
Requires:         R-CRAN-stringi >= 1.7.12
Requires:         R-CRAN-glue >= 1.6.2
Requires:         R-CRAN-stringr >= 1.5.0
Requires:         R-CRAN-scales >= 1.2.1
Requires:         R-CRAN-purrr >= 1.0.1
Requires:         R-CRAN-htmltools >= 0.5.5
Requires:         R-CRAN-fontawesome >= 0.5.0
Requires:         R-CRAN-reactable >= 0.4.4

%description
Simple and flexible quizzes in 'shiny'. Easily create quizzes from various
pre-built question and choice types or create your own using 'htmltools'
and 'shiny' packages as building blocks. Integrates with larger 'shiny'
applications. Ideal for non-web-developers such as educators, data
scientists, and anyone who wants to assess responses interactively in a
small form factor.

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
