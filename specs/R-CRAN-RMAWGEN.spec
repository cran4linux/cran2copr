%global packname  RMAWGEN
%global packver   1.3.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.7
Release:          2%{?dist}
Summary:          Multi-Site Auto-Regressive Weather GENerator

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-chron 
BuildRequires:    R-CRAN-date 
BuildRequires:    R-CRAN-vars 
BuildRequires:    R-methods 
Requires:         R-CRAN-chron 
Requires:         R-CRAN-date 
Requires:         R-CRAN-vars 
Requires:         R-methods 

%description
S3 and S4 functions are implemented for spatial multi-site stochastic
generation of daily time series of temperature and precipitation. These
tools make use of Vector AutoRegressive models (VARs). The weather
generator model is then saved as an object and is calibrated by daily
instrumental "Gaussianized" time series through the 'vars' package tools.
Once obtained this model, it can it can be used for weather generations
and be adapted to work with several climatic monthly time series.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
