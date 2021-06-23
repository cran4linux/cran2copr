%global __brp_check_rpaths %{nil}
%global packname  randomNames
%global packver   1.5-0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Generate Random Given and Surnames

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.14.0
BuildRequires:    R-CRAN-toOrdinal >= 1.1
BuildRequires:    R-CRAN-crayon 
Requires:         R-CRAN-data.table >= 1.14.0
Requires:         R-CRAN-toOrdinal >= 1.1
Requires:         R-CRAN-crayon 

%description
Function for generating random gender and ethnicity correct first and/or
last names. Names are chosen proportionally based upon their probability
of appearing in a large scale data base of real names.

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
