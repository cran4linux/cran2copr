%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  muRL
%global packver   0.1-13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.13
Release:          1%{?dist}%{?buildtag}
Summary:          Mailmerge using R, LaTeX, and the Web

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-graphics 
Requires:         R-utils 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-stringr 
Requires:         R-graphics 

%description
Provides mailmerge methods for reading spreadsheets of addresses and other
relevant information to create standardized but customizable letters.
Provides a method for mapping US ZIP codes, including those of letter
recipients.  Provides a method for parsing and processing html code from
online job postings of the American Political Science Association.

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
