%global packname  geonames
%global packver   0.999
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.999
Release:          3%{?dist}
Summary:          Interface to the "Geonames" Spatial Query Web Service

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.2.0
Requires:         R-core >= 2.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rjson 
Requires:         R-CRAN-rjson 

%description
The web service at <https://www.geonames.org/> provides a number of
spatial data queries, including administrative area hierarchies, city
locations and some country postal code queries. A (free) username is
required and rate limits exist.

%prep
%setup -q -c -n %{packname}


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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/tests
%{rlibdir}/%{packname}/INDEX
