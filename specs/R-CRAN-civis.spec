%global packname  civis
%global packver   3.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0
Release:          2%{?dist}
Summary:          R Client for the 'Civis Platform API'

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-future >= 1.8.0
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-future >= 1.8.0
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-methods 
Requires:         R-CRAN-memoise 
Requires:         R-stats 
Requires:         R-utils 

%description
A convenient interface for making requests directly to the 'Civis Platform
API' <https://www.civisanalytics.com/platform/>. Full documentation
available 'here' <https://civisanalytics.github.io/civis-r/>.

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

%files
%{rlibdir}/%{packname}
