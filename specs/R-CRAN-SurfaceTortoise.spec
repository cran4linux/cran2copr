%global packname  SurfaceTortoise
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          2%{?dist}
Summary:          Find Optimal Sampling Locations Based on Spatial Covariate(s)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.4
Requires:         R-core >= 3.4.4
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-sp 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-gstat 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-sp 

%description
Create sampling designs using the surface reconstruction algorithm.
Original method by: Olsson, D. 2002. A method to optimize soil sampling
from ancillary data. Poster presenterad at: NJF seminar no. 336,
Implementation of Precision Farming in Practical Agriculture, 10-12 June
2002, Skara, Sweden.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
