%global __brp_check_rpaths %{nil}
%global packname  languageserver
%global packver   0.3.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.10
Release:          1%{?dist}%{?buildtag}
Summary:          Language Server Protocol

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-roxygen2 >= 7.0.0
BuildRequires:    R-CRAN-callr >= 3.0.0
BuildRequires:    R-CRAN-R6 >= 2.4.1
BuildRequires:    R-CRAN-lintr >= 2.0.0
BuildRequires:    R-CRAN-jsonlite >= 1.6
BuildRequires:    R-CRAN-styler >= 1.4.1
BuildRequires:    R-CRAN-fs >= 1.3.1
BuildRequires:    R-CRAN-xml2 >= 1.2.2
BuildRequires:    R-CRAN-desc >= 1.2.0
BuildRequires:    R-CRAN-stringi >= 1.1.7
BuildRequires:    R-CRAN-repr >= 1.1.0
BuildRequires:    R-CRAN-xmlparsedata >= 1.0.3
BuildRequires:    R-CRAN-collections >= 0.3.0
BuildRequires:    R-parallel 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-roxygen2 >= 7.0.0
Requires:         R-CRAN-callr >= 3.0.0
Requires:         R-CRAN-R6 >= 2.4.1
Requires:         R-CRAN-lintr >= 2.0.0
Requires:         R-CRAN-jsonlite >= 1.6
Requires:         R-CRAN-styler >= 1.4.1
Requires:         R-CRAN-fs >= 1.3.1
Requires:         R-CRAN-xml2 >= 1.2.2
Requires:         R-CRAN-desc >= 1.2.0
Requires:         R-CRAN-stringi >= 1.1.7
Requires:         R-CRAN-repr >= 1.1.0
Requires:         R-CRAN-xmlparsedata >= 1.0.3
Requires:         R-CRAN-collections >= 0.3.0
Requires:         R-parallel 
Requires:         R-tools 
Requires:         R-utils 

%description
An implementation of the Language Server Protocol for R. The Language
Server protocol is used by an editor client to integrate features like
auto completion. See
<https://microsoft.github.io/language-server-protocol/> for details.

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
