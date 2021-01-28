%global packname  mlr3oml
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Connector Between 'mlr3' and 'OpenML'

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-backports >= 1.1.6
BuildRequires:    R-CRAN-mlr3misc >= 0.7.0
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-lgr 
BuildRequires:    R-CRAN-mlr3 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-stringi 
Requires:         R-CRAN-backports >= 1.1.6
Requires:         R-CRAN-mlr3misc >= 0.7.0
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-lgr 
Requires:         R-CRAN-mlr3 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-stringi 

%description
Provides an interface to 'OpenML.org' to list and download machine
learning data and tasks. Data and tasks can be automatically converted to
'mlr3' tasks. For a more sophisticated interface which also allows
uploading experiments, see the 'OpenML' package.

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
