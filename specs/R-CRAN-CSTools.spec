%global packname  CSTools
%global packver   3.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0
Release:          1%{?dist}
Summary:          Assessing Skill of Climate Forecasts on Seasonal-to-DecadalTimescales

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.2
Requires:         R-core >= 3.4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-s2dverification 
BuildRequires:    R-CRAN-rainfarmr 
BuildRequires:    R-CRAN-multiApply 
BuildRequires:    R-CRAN-qmap 
BuildRequires:    R-CRAN-ClimProjDiags 
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-verification 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-s2dverification 
Requires:         R-CRAN-rainfarmr 
Requires:         R-CRAN-multiApply 
Requires:         R-CRAN-qmap 
Requires:         R-CRAN-ClimProjDiags 
Requires:         R-CRAN-ncdf4 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-verification 

%description
Exploits dynamical seasonal forecasts in order to provide information
relevant to stakeholders at the seasonal timescale. The package contains
process-based methods for forecast calibration, bias correction,
statistical and stochastic downscaling, optimal forecast combination and
multivariate verification, as well as basic and advanced tools to obtain
tailored products. This package was developed in the context of the ERA4CS
project MEDSCOPE and the H2020 S2S4E project. Doblas-Reyes et al. (2005)
<doi:10.1111/j.1600-0870.2005.00104.x>. Mishra et al. (2018)
<doi:10.1007/s00382-018-4404-z>. Sanchez-Garcia et al. (2019)
<doi:10.5194/asr-16-165-2019>. Straus et al. (2007)
<doi:10.1175/JCLI4070.1>. Terzago et al. (2018)
<doi:10.5194/nhess-18-2825-2018>. Torralba et al. (2017)
<doi:10.1175/JAMC-D-16-0204.1>. D'Onofrio et al. (2014)
<doi:10.1175/JHM-D-13-096.1>. Van Schaeybroeck et al. (2019)
<doi:10.1016/B978-0-12-812372-0.00010-8>. Yiou et al. (2013)
<doi:10.1007/s00382-012-1626-3>.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
