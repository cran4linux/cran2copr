%global packname  crimeutils
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Comprehensive Set of Functions to Clean, Analyze, and Present Crime Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-gt 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-janitor 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-gt 
Requires:         R-grDevices 
Requires:         R-CRAN-tidyr 
Requires:         R-stats 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-janitor 

%description
A collection of functions that make it easier to understand crime (or
other) data, and assist others in understanding it. The package helps you
read data from various sources, clean it, fix column names, and graph the
data.

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
