%global packname  spacom
%global packver   1.0-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}
Summary:          Spatially Weighted Context Data for Multilevel Modelling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.3.2
Requires:         R-core >= 2.3.2
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-nlme 
BuildRequires:    R-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-lme4 
Requires:         R-nlme 
Requires:         R-Matrix 

%description
Provides tools to construct and exploit spatially weighted context data.
Spatial weights are derived by a Kernel function from a user-defined
matrix of distances between contextual units. Spatial weights can then be
applied either to precise contextual measures or to aggregate estimates
based on micro-level survey data, to compute spatially weighted context
data. Available aggregation functions include indicators of central
tendency, dispersion, or inter-group variability, and take into account
survey design weights. The package further allows combining the resulting
spatially weighted context data with individual-level predictor and
outcome variables, for the purposes of multilevel modelling. An ad hoc
stratified bootstrap resampling procedure generates robust point estimates
for multilevel regression coefficients and model fit indicators, and
computes confidence intervals adjusted for measurement dependency and
measurement error of aggregate estimates. As an additional feature,
residual and explained spatial dependency can be estimated for the tested
models.

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
