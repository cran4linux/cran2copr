%global __brp_check_rpaths %{nil}
%global packname  geoGAM
%global packver   0.1-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Select Sparse Geoadditive Models for Spatial Prediction

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mboost 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-grpreg 
BuildRequires:    R-MASS 
Requires:         R-CRAN-mboost 
Requires:         R-mgcv 
Requires:         R-CRAN-grpreg 
Requires:         R-MASS 

%description
A model building procedure to build parsimonious geoadditive model from a
large number of covariates. Continuous, binary and ordered categorical
responses are supported. The model building is based on component wise
gradient boosting with linear effects, smoothing splines and a smooth
spatial surface to model spatial autocorrelation. The resulting covariate
set after gradient boosting is further reduced through backward
elimination and aggregation of factor levels. The package provides a model
based bootstrap method to simulate prediction intervals for point
predictions. A test data set of a soil mapping case study in Berne
(Switzerland) is provided.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
