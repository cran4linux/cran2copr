%global packname  geojsonlint
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          3%{?dist}
Summary:          Tools for Validating 'GeoJSON'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonvalidate >= 1.0.0
BuildRequires:    R-CRAN-jsonlite >= 0.9.19
BuildRequires:    R-CRAN-crul >= 0.7.0
BuildRequires:    R-CRAN-V8 
Requires:         R-CRAN-jsonvalidate >= 1.0.0
Requires:         R-CRAN-jsonlite >= 0.9.19
Requires:         R-CRAN-crul >= 0.7.0
Requires:         R-CRAN-V8 

%description
Tools for linting 'GeoJSON'. Includes tools for interacting with the
online tool <http://geojsonlint.com>, the 'Javascript' library
'geojsonhint' (<https://www.npmjs.com/package/geojsonhint>), and
validating against a 'GeoJSON' schema via the 'Javascript' library
(<https://www.npmjs.com/package/is-my-json-valid>). Some tools work
locally while others require an internet connection.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/img
%doc %{rlibdir}/%{packname}/js
%doc %{rlibdir}/%{packname}/schema
%{rlibdir}/%{packname}/INDEX
