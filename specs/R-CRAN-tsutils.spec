%global packname  tsutils
%global packver   0.9.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.2
Release:          1%{?dist}
Summary:          Time Series Exploration, Modelling and Forecasting

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-MAPA 
BuildRequires:    R-CRAN-plotrix 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-MAPA 
Requires:         R-CRAN-plotrix 

%description
Includes: (i) tests and visualisations that can help the modeller explore
time series components and perform decomposition; (ii) modelling
shortcuts, such as functions to construct lagmatrices and seasonal dummy
variables of various forms; (iii) an implementation of the Theta method;
(iv) tools to facilitate the design of the forecasting process, such as
ABC-XYZ analyses; and (v) "quality of life" functions, such as treating
time series for trailing and leading values.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
