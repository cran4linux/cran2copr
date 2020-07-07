%global packname  datarobot
%global packver   2.17.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.17.1
Release:          2%{?dist}
Summary:          'DataRobot' Predictive Modeling API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildArch:        noarch
BuildRequires:    R-CRAN-yaml >= 2.1.13
BuildRequires:    R-CRAN-httr >= 1.2.0
BuildRequires:    R-CRAN-jsonlite >= 1.0
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-yaml >= 2.1.13
Requires:         R-CRAN-httr >= 1.2.0
Requires:         R-CRAN-jsonlite >= 1.0
Requires:         R-methods 
Requires:         R-stats 

%description
For working with the 'DataRobot' predictive modeling platform's API
<https://www.datarobot.com/>.

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
