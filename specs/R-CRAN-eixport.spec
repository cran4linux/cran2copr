%global packname  eixport
%global packver   0.4.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.6
Release:          1%{?dist}
Summary:          Export Emissions to Atmospheric Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-silicate >= 0.3
BuildRequires:    R-CRAN-sfheaders >= 0.2.1
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-cptcity 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-silicate >= 0.3
Requires:         R-CRAN-sfheaders >= 0.2.1
Requires:         R-CRAN-sf 
Requires:         R-CRAN-ncdf4 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sp 
Requires:         R-methods 
Requires:         R-CRAN-cptcity 
Requires:         R-utils 
Requires:         R-CRAN-tidyr 

%description
Emissions are the mass of pollutants released into the atmosphere. Air
quality models need emissions data, with spatial and temporal
distribution, to represent air pollutant concentrations. This package,
eixport, creates inputs for the air quality models 'WRF-Chem' Grell et al
(2005) <doi:10.1016/j.atmosenv.2005.04.027>, 'BRAMS-SPM' Freitas et al
(2005) <doi:10.1016/j.atmosenv.2005.07.017> and 'RLINE' Snyder et al
(2013) <doi:10.1016/j.atmosenv.2013.05.074>. See the eixport website
(<https://atmoschem.github.io/eixport/>) for more information,
documentations and examples. More details in Ibarra-Espinosa et al (2018)
<doi.org/10.21105/joss.00607>.

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
