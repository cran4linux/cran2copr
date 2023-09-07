%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  censobr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Download Data from Brazil's Population Census

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr >= 1.4.1
BuildRequires:    R-CRAN-arrow 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-tools 
Requires:         R-CRAN-httr >= 1.4.1
Requires:         R-CRAN-arrow 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-dplyr 
Requires:         R-tools 

%description
Download data from Brazil's population census. The package is built on top
of the 'Arrow' platform <https://arrow.apache.org/docs/r/>, which allows
users to work with larger-than-memory census data using 'dplyr' familiar
functions.
<https://arrow.apache.org/docs/r/articles/arrow.html#analyzing-arrow-data-with-dplyr>.

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
