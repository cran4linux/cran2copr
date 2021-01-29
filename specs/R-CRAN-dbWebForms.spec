%global packname  dbWebForms
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Produce R Functions to Create HTML Forms Based on SQL Meta Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-html5 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-html5 

%description
Offers meta programming style tools to generate configurable R functions
that produce HTML forms based on table input and SQL meta data. Also
generates functions for collecting the parameters of those HTML forms
after they are submitted. Useful for quickly generating HTML forms based
on existing SQL tables. To use the resultant functions, the output files
containing those functions must be read into the R environment (perhaps
using base::source()).

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
