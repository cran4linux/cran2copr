%global packname  distreg.vis
%global packver   1.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.0
Release:          1%{?dist}
Summary:          Framework for the Visualization of Distributional RegressionModels

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gamlss.dist >= 5.1.0
BuildRequires:    R-CRAN-gamlss >= 5.0.6
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-formatR >= 1.5
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.2
BuildRequires:    R-CRAN-mvtnorm >= 1.0.6
BuildRequires:    R-CRAN-shiny >= 1.0.3
BuildRequires:    R-CRAN-viridis >= 0.4.0
BuildRequires:    R-CRAN-rhandsontable >= 0.3.4
BuildRequires:    R-CRAN-bamlss >= 0.1.2
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
Requires:         R-CRAN-gamlss.dist >= 5.1.0
Requires:         R-CRAN-gamlss >= 5.0.6
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-formatR >= 1.5
Requires:         R-CRAN-RColorBrewer >= 1.1.2
Requires:         R-CRAN-mvtnorm >= 1.0.6
Requires:         R-CRAN-shiny >= 1.0.3
Requires:         R-CRAN-viridis >= 0.4.0
Requires:         R-CRAN-rhandsontable >= 0.3.4
Requires:         R-CRAN-bamlss >= 0.1.2
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-methods 

%description
Functions for visualizing distributional regression models fitted using
the 'gamlss' or 'bamlss' R package. The core of the package consists of a
'shiny' application, where the model results can be interactively explored
and visualized.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/rstudio
%doc %{rlibdir}/%{packname}/srcjs
%{rlibdir}/%{packname}/INDEX
