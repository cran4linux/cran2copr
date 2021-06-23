%global __brp_check_rpaths %{nil}
%global packname  UKgrid
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          2%{?dist}%{?buildtag}
Summary:          The UK National Electricity Transmission System Dataset

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-zoo >= 1.8.0
BuildRequires:    R-CRAN-lubridate >= 1.6.0
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-data.table >= 1.11.2
BuildRequires:    R-CRAN-tsibble >= 0.9.0
BuildRequires:    R-CRAN-dplyr >= 0.7.5
BuildRequires:    R-CRAN-xts >= 0.12.0
Requires:         R-CRAN-zoo >= 1.8.0
Requires:         R-CRAN-lubridate >= 1.6.0
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-data.table >= 1.11.2
Requires:         R-CRAN-tsibble >= 0.9.0
Requires:         R-CRAN-dplyr >= 0.7.5
Requires:         R-CRAN-xts >= 0.12.0

%description
A time series of the national grid demand (high-voltage electric power
transmission network) in the UK since 2011.

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
