%global __brp_check_rpaths %{nil}
%global packname  riem
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Accesses Weather Data from the Iowa Environment Mesonet

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lubridate >= 1.5.6
BuildRequires:    R-CRAN-httr >= 1.1.0
BuildRequires:    R-CRAN-jsonlite >= 0.9.19
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-lubridate >= 1.5.6
Requires:         R-CRAN-httr >= 1.1.0
Requires:         R-CRAN-jsonlite >= 0.9.19
Requires:         R-CRAN-tibble 

%description
Allows to get weather data from Automated Surface Observing System (ASOS)
stations (airports) in the whole world thanks to the Iowa Environment
Mesonet website.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
