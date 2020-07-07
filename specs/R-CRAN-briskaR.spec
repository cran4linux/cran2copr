%global packname  briskaR
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}
Summary:          Biological Risk Assessment

License:          GPL (>= 2) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3.29
BuildRequires:    R-CRAN-fields >= 7.1
BuildRequires:    R-stats >= 3.0.2
BuildRequires:    R-grDevices >= 3.0.0
BuildRequires:    R-graphics >= 3.0.0
BuildRequires:    R-CRAN-raster >= 2.3.0
BuildRequires:    R-CRAN-pracma >= 1.8.3
BuildRequires:    R-CRAN-mvtnorm >= 1.0.2
BuildRequires:    R-CRAN-sp >= 1.0.17
BuildRequires:    R-CRAN-fftwtools >= 0.9.6
BuildRequires:    R-CRAN-rgdal >= 0.9
BuildRequires:    R-CRAN-rgeos >= 0.3
BuildRequires:    R-CRAN-deldir >= 0.1
BuildRequires:    R-methods 
Requires:         R-MASS >= 7.3.29
Requires:         R-CRAN-fields >= 7.1
Requires:         R-stats >= 3.0.2
Requires:         R-grDevices >= 3.0.0
Requires:         R-graphics >= 3.0.0
Requires:         R-CRAN-raster >= 2.3.0
Requires:         R-CRAN-pracma >= 1.8.3
Requires:         R-CRAN-mvtnorm >= 1.0.2
Requires:         R-CRAN-sp >= 1.0.17
Requires:         R-CRAN-fftwtools >= 0.9.6
Requires:         R-CRAN-rgdal >= 0.9
Requires:         R-CRAN-rgeos >= 0.3
Requires:         R-CRAN-deldir >= 0.1
Requires:         R-methods 

%description
A spatio-temporal exposure-hazard model for assessing biological risk and
impact. The model is based on stochastic geometry for describing the
landscape and the exposed individuals, a dispersal kernel for the
dissemination of contaminants and an ecotoxicological equation. Walker E,
Leclerc M, Rey JF, Beaudouin R, Soubeyrand S, and Messean A, (2017), A
Spatio-Temporal Exposure-Hazard Model for Assessing Biological Risk and
Impact, Risk Analysis, <doi:10.1111/risa.12941>.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
