%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  adbi
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          'DBI' Compliant Database Access Using 'ADBC'

License:          LGPL (>= 2.1)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DBI >= 1.2.0
BuildRequires:    R-CRAN-adbcdrivermanager >= 0.8.0
BuildRequires:    R-CRAN-nanoarrow >= 0.3.0
BuildRequires:    R-methods 
Requires:         R-CRAN-DBI >= 1.2.0
Requires:         R-CRAN-adbcdrivermanager >= 0.8.0
Requires:         R-CRAN-nanoarrow >= 0.3.0
Requires:         R-methods 

%description
In order to make Arrow Database Connectivity ('ADBC'
<https://arrow.apache.org/adbc/>) accessible from R, an interface
compliant with the 'DBI' package is provided, using driver back-ends that
are implemented in the 'adbcdrivermanager' framework. This enables
interacting with database systems using the Arrow data format, thereby
offering an efficient alternative to 'ODBC' for analytical applications.

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
