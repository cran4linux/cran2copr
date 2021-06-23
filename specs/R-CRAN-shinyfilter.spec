%global __brp_check_rpaths %{nil}
%global packname  shinyfilter
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Use Interdependent Filters on Table Columns in Shiny Apps

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-reactable 
BuildRequires:    R-CRAN-shinyBS 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-reactable 
Requires:         R-CRAN-shinyBS 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-stringr 

%description
Allows to connect 'selectizeInputs' widgets as filters to a 'reactable'
table. As known from spreadsheet applications, column filters are
interdependent, so each filter only shows the values that are really
available at the moment based on the current selection in other filters.
Filter values currently not available (and also those being available) can
be shown via popovers or tooltips.

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
