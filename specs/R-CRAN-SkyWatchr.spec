%global packname  SkyWatchr
%global packver   0.8-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.2
Release:          1%{?dist}
Summary:          Search and Download Satellite Imagery using the SkyWatch API

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-htmlTable 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-methods 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-htmlTable 
Requires:         R-CRAN-sp 
Requires:         R-methods 

%description
Query and download satellite imagery and climate/atmospheric datasets
using the SkyWatch API. Search datasets by wavelength (band), cloud cover,
resolution, location, date, etc. Get the query results as data frame and
as HTML. To learn more about the SkyWatch API, see
<https://github.com/skywatchspaceapps/api>.

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
%{rlibdir}/%{packname}/INDEX
