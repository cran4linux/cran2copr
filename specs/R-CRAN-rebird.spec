%global packname  rebird
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}
Summary:          R Client for the eBird Database of Bird Observations

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-httr >= 1.0.0
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-assertthat 
Requires:         R-CRAN-httr >= 1.0.0
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-assertthat 

%description
A programmatic client for the eBird database, including functions for
searching for bird observations by geographic location (latitude,
longitude), eBird hotspots, location identifiers, by notable sightings, by
region, and by taxonomic name.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/vign
%{rlibdir}/%{packname}/INDEX
