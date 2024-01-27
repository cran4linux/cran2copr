%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  smallstuff
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Dr. Small's Functions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-class >= 7.3.20
BuildRequires:    R-CRAN-Matrix >= 1.4.1
BuildRequires:    R-CRAN-igraph >= 1.3.1
BuildRequires:    R-CRAN-data.table >= 1.14.2
BuildRequires:    R-CRAN-ROCR >= 1.0.11
BuildRequires:    R-CRAN-matlib >= 0.9.5
BuildRequires:    R-CRAN-pryr >= 0.1.5
Requires:         R-CRAN-class >= 7.3.20
Requires:         R-CRAN-Matrix >= 1.4.1
Requires:         R-CRAN-igraph >= 1.3.1
Requires:         R-CRAN-data.table >= 1.14.2
Requires:         R-CRAN-ROCR >= 1.0.11
Requires:         R-CRAN-matlib >= 0.9.5
Requires:         R-CRAN-pryr >= 0.1.5

%description
Functions used in courses taught by Dr. Small at Drew University.

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
