%global packname  RmarineHeatWaves
%global packver   0.17.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.17.0
Release:          2%{?dist}
Summary:          Detect Marine Heat Waves and Marine Cold Spells

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.00
Requires:         R-core >= 3.00
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-dplyr 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-raster 
Requires:         R-grid 
Requires:         R-CRAN-lazyeval 
Requires:         R-CRAN-rlang 

%description
Given a time series of daily temperatures, the package provides tools to
detect extreme thermal events, including marine heat waves, and to
calculate the exceedances above or below specified threshold values. It
outputs the properties of all detected events and exceedances.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
