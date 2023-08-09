%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  naijR
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Operations to Ease Data Analyses Specific to Nigeria

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-CRAN-maps >= 3.3.0
BuildRequires:    R-CRAN-mapdata >= 2.3.0
BuildRequires:    R-CRAN-stringi >= 1.7.6
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.2
BuildRequires:    R-CRAN-sf >= 1.0.13
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-lifecycle >= 0.2.0
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-maps >= 3.3.0
Requires:         R-CRAN-mapdata >= 2.3.0
Requires:         R-CRAN-stringi >= 1.7.6
Requires:         R-CRAN-RColorBrewer >= 1.1.2
Requires:         R-CRAN-sf >= 1.0.13
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-lifecycle >= 0.2.0
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-utils 

%description
A set of convenience functions as well as geographical/political data
about Nigeria, aimed at simplifying work with data and information that
are specific to the country.

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
