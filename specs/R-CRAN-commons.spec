%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  commons
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          AI Agents for Data Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-duckdb >= 1.5.4.2
BuildRequires:    R-CRAN-promises >= 1.5.0
BuildRequires:    R-CRAN-rlang >= 1.2.0
BuildRequires:    R-CRAN-httr2 >= 1.1.0
BuildRequires:    R-CRAN-ellmer >= 0.5.0
BuildRequires:    R-CRAN-shinychat >= 0.5.0
BuildRequires:    R-CRAN-bslib >= 0.11.0
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-coro 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-evaluate 
BuildRequires:    R-CRAN-filelock 
BuildRequires:    R-CRAN-highr 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-later 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-processx 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-ragg 
BuildRequires:    R-CRAN-ragnar 
BuildRequires:    R-CRAN-roxygen2 
BuildRequires:    R-CRAN-S7 
BuildRequires:    R-CRAN-sass 
BuildRequires:    R-utils 
Requires:         R-CRAN-duckdb >= 1.5.4.2
Requires:         R-CRAN-promises >= 1.5.0
Requires:         R-CRAN-rlang >= 1.2.0
Requires:         R-CRAN-httr2 >= 1.1.0
Requires:         R-CRAN-ellmer >= 0.5.0
Requires:         R-CRAN-shinychat >= 0.5.0
Requires:         R-CRAN-bslib >= 0.11.0
Requires:         R-CRAN-callr 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-coro 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-evaluate 
Requires:         R-CRAN-filelock 
Requires:         R-CRAN-highr 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-later 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-processx 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-ragg 
Requires:         R-CRAN-ragnar 
Requires:         R-CRAN-roxygen2 
Requires:         R-CRAN-S7 
Requires:         R-CRAN-sass 
Requires:         R-utils 

%description
Implements trustworthy large language model agents. Connect raw data
sources, a pool of trusted calculations, and a searchable context layer
that demonstrates how to interpret them. Then, deploy data agents that
answer questions, log interactions, and can be evaluated and improved over
time.

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
