%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  querychat
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Filter and Query Data Frames in 'shiny' Using an LLM Chat Interface

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-ellmer >= 0.3.0
BuildRequires:    R-CRAN-shinychat >= 0.3.0
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-promises 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-S7 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-whisker 
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-ellmer >= 0.3.0
Requires:         R-CRAN-shinychat >= 0.3.0
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-promises 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-S7 
Requires:         R-CRAN-shiny 
Requires:         R-utils 
Requires:         R-CRAN-whisker 

%description
Adds an LLM-powered chatbot to your 'shiny' app, that can turn your users'
natural language questions into SQL queries that run against your data,
and return the result as a reactive data frame. Use it to drive reactive
calculations, visualizations, downloads, and more.

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
