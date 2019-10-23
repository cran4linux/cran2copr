%global packname  mtsdi
%global packver   0.3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.5
Release:          1%{?dist}
Summary:          Multivariate Time Series Data Imputation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-gam 
BuildRequires:    R-splines 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-gam 
Requires:         R-splines 

%description
This is an EM algorithm based method for imputation of missing values in
multivariate normal time series. The imputation algorithm accounts for
both spatial and temporal correlation structures. Temporal patterns can be
modeled using an ARIMA(p,d,q), optionally with seasonal components, a
non-parametric cubic spline or generalized additive models with exogenous
covariates. This algorithm is specially tailored for climate data with
missing measurements from several monitors along a given region.

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
