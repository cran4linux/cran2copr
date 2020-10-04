%global packname  EmissV
%global packver   0.665.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.665.2.1
Release:          3%{?dist}%{?buildtag}
Summary:          Vehicular Emissions by Top-Down Methods

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-units >= 0.5.1
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-units >= 0.5.1
Requires:         R-CRAN-ncdf4 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-sf 
Requires:         R-methods 
Requires:         R-CRAN-data.table 

%description
Creates emissions for use in air quality models. Vehicular emissions are
estimated by a top-down approach, total emissions are calculated using the
statistical description of the fleet of vehicles, the emission is
spatially distributed according to satellite images or openstreetmap data
<https://www.openstreetmap.org> and then distributed temporarily
(Vara-Vela et al., 2016, <doi:10.5194/acp-16-777-2016>).

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
