%global __brp_check_rpaths %{nil}
%global packname  lue
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          3%{?dist}%{?buildtag}
Summary:          Light Use Efficiency Model to Estimate Biomass and YIELD withand Without Vapour Pressure Deficit

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-ncdf4 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-ncdf4 

%description
Contains LUE_BIOMASS(),LUE_BIOMASS_VPD(), LUE_YIELD() and LUE_YIELD_VPD()
to estimate aboveground biomass and crop yield firstly by calculating the
Absorbed Photosynthetically Active Radiation (APAR) and secondly the
actual values of light use efficiency with and without vapour presure
deficit Shi et al.(2007) <doi:10.2134/agronj2006.0260>.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
