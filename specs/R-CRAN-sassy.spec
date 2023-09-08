%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sassy
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Makes 'R' Easier for Everyone

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-common 
BuildRequires:    R-CRAN-logr 
BuildRequires:    R-CRAN-fmtr 
BuildRequires:    R-CRAN-libr 
BuildRequires:    R-CRAN-reporter 
BuildRequires:    R-CRAN-procs 
BuildRequires:    R-datasets 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-common 
Requires:         R-CRAN-logr 
Requires:         R-CRAN-fmtr 
Requires:         R-CRAN-libr 
Requires:         R-CRAN-reporter 
Requires:         R-CRAN-procs 
Requires:         R-datasets 
Requires:         R-tools 
Requires:         R-utils 

%description
A meta-package that aims to make 'R' easier for everyone, especially
programmers who have a background in 'SAS®' software. This set of packages
brings many useful concepts to 'R', including data libraries, data
dictionaries, formats and format catalogs, a data step, and a traceable
log.  The 'flagship' package is a reporting package that can output in
text, rich text, 'PDF', 'HTML', and 'DOCX' file formats.

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
