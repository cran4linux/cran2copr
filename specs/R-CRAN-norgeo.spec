%global __brp_check_rpaths %{nil}
%global packname  norgeo
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Track Geo Code Changes in all Regional Granularity in Norway

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.14.0
BuildRequires:    R-CRAN-odbc 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-writexl 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-data.table >= 1.14.0
Requires:         R-CRAN-odbc 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-writexl 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 

%description
Regional granularity levels in Norway which are depicted by different
codes, have undergone several changes over the years. Identifying when
codes have changed and how many changes have taken place can be
troublesome. This package will help to identify these changes and when the
changes have taken place. One of the limitation of this package is that it
is heavily depending on the codes available from SSB website
<https://data.ssb.no/api/klass/v1/api-guide.html>.

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
