%global packname  biomod2
%global packver   3.4.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.4.6
Release:          3%{?dist}%{?buildtag}
Summary:          Ensemble Platform for Species Distribution Modeling

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gbm >= 2.1.3
BuildRequires:    R-CRAN-pROC >= 1.15.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-rasterVis 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-mda 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-rpart 
BuildRequires:    R-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-PresenceAbsence 
BuildRequires:    R-CRAN-dismo 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-ENMeval 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-earth 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-maxnet 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-gbm >= 2.1.3
Requires:         R-CRAN-pROC >= 1.15.0
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-lattice 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-raster 
Requires:         R-parallel 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-rasterVis 
Requires:         R-nnet 
Requires:         R-CRAN-mda 
Requires:         R-CRAN-randomForest 
Requires:         R-rpart 
Requires:         R-MASS 
Requires:         R-methods 
Requires:         R-CRAN-PresenceAbsence 
Requires:         R-CRAN-dismo 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-ENMeval 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-earth 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-maxnet 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 

%description
Functions for species distribution modeling, calibration and evaluation,
ensemble of models, ensemble forecasting and visualization. The package
permits to run consistently up to 10 single models on a presence/absences
(resp presences/pseudo-absences) dataset and to combine them in ensemble
models and ensemble projections. Some bench of other evaluation and
visualisation tools are also available within the package.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/external
%doc %{rlibdir}/%{packname}/HasBeenCustom.txt
%{rlibdir}/%{packname}/INDEX
%doc %{rlibdir}/%{packname}/HasBeenCustom.txt
