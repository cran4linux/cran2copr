%global packname  biomod2
%global packver   3.3-7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.3.7.1
Release:          1%{?dist}
Summary:          Ensemble Platform for Species Distribution Modeling

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.1
Requires:         R-core >= 3.2.1
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-rasterVis 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-CRAN-mda 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-rpart 
BuildRequires:    R-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-PresenceAbsence 
BuildRequires:    R-CRAN-dismo 
BuildRequires:    R-CRAN-earth 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-raster 
Requires:         R-parallel 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-rasterVis 
Requires:         R-CRAN-pROC 
Requires:         R-nnet 
Requires:         R-CRAN-gbm 
Requires:         R-CRAN-mda 
Requires:         R-CRAN-randomForest 
Requires:         R-rpart 
Requires:         R-MASS 
Requires:         R-methods 
Requires:         R-CRAN-PresenceAbsence 
Requires:         R-CRAN-dismo 
Requires:         R-CRAN-earth 

%description
Functions for species distribution modeling, calibration and evaluation,
ensemble of models.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/external
%{rlibdir}/%{packname}/INDEX
%doc %{rlibdir}/%{packname}/HasBeenCustom.txt
