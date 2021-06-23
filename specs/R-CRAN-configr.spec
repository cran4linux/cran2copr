%global __brp_check_rpaths %{nil}
%global packname  configr
%global packver   0.3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.5
Release:          1%{?dist}%{?buildtag}
Summary:          An Implementation of Parsing and Writing Configuration File(JSON/INI/YAML/TOML)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-yaml >= 2.1.3
BuildRequires:    R-CRAN-stringr >= 1.2.0
BuildRequires:    R-CRAN-jsonlite >= 1.2
BuildRequires:    R-CRAN-ini >= 0.2
BuildRequires:    R-CRAN-RcppTOML >= 0.1.3
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-glue 
Requires:         R-CRAN-yaml >= 2.1.3
Requires:         R-CRAN-stringr >= 1.2.0
Requires:         R-CRAN-jsonlite >= 1.2
Requires:         R-CRAN-ini >= 0.2
Requires:         R-CRAN-RcppTOML >= 0.1.3
Requires:         R-utils 
Requires:         R-CRAN-glue 

%description
Implements the JSON, INI, YAML and TOML parser for R setting and writing
of configuration file. The functionality of this package is similar to
that of package 'config'.

%prep
%setup -q -c -n %{packname}
find %{packname} -type f -exec sed -Ei 's@#!( )*(/usr)*/bin/(env )*python@#!/usr/bin/python2@g' {} \;
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
