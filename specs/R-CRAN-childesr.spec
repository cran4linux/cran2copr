%global __brp_check_rpaths %{nil}
%global packname  childesr
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Accessing the 'CHILDES' Database

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dbplyr >= 2.1
BuildRequires:    R-CRAN-magrittr >= 2.0
BuildRequires:    R-CRAN-jsonlite >= 1.7
BuildRequires:    R-CRAN-DBI >= 1.1
BuildRequires:    R-CRAN-dplyr >= 1.0
BuildRequires:    R-CRAN-purrr >= 0.3
BuildRequires:    R-CRAN-RMySQL >= 0.10.21
Requires:         R-CRAN-dbplyr >= 2.1
Requires:         R-CRAN-magrittr >= 2.0
Requires:         R-CRAN-jsonlite >= 1.7
Requires:         R-CRAN-DBI >= 1.1
Requires:         R-CRAN-dplyr >= 1.0
Requires:         R-CRAN-purrr >= 0.3
Requires:         R-CRAN-RMySQL >= 0.10.21

%description
Tools for connecting to 'CHILDES', an open repository for transcripts of
parent-child interaction. For more information on the underlying data, see
<https://childes-db.stanford.edu>.

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
