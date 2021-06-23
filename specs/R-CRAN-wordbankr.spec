%global __brp_check_rpaths %{nil}
%global packname  wordbankr
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Accessing the Wordbank Database

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dbplyr >= 1.4.4
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-tidyr >= 1.1.2
BuildRequires:    R-CRAN-DBI >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 1.0.2
BuildRequires:    R-CRAN-robustbase >= 0.93
BuildRequires:    R-CRAN-rlang >= 0.4.8
BuildRequires:    R-CRAN-quantregGrowth >= 0.4
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-assertthat >= 0.2.1
BuildRequires:    R-CRAN-RMySQL >= 0.10.20
Requires:         R-CRAN-dbplyr >= 1.4.4
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-tidyr >= 1.1.2
Requires:         R-CRAN-DBI >= 1.1.0
Requires:         R-CRAN-dplyr >= 1.0.2
Requires:         R-CRAN-robustbase >= 0.93
Requires:         R-CRAN-rlang >= 0.4.8
Requires:         R-CRAN-quantregGrowth >= 0.4
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-assertthat >= 0.2.1
Requires:         R-CRAN-RMySQL >= 0.10.20

%description
Tools for connecting to Wordbank, an open repository for developmental
vocabulary data. For more information on the underlying data, see
<http://wordbank.stanford.edu>.

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
