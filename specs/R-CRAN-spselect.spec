%global packname  spselect
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          2%{?dist}
Summary:          Selecting Spatial Scale of Covariates in Regression Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tester 
BuildRequires:    R-CRAN-magic 
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-tester 
Requires:         R-CRAN-magic 
Requires:         R-CRAN-pracma 

%description
Fits spatial scale (SS) forward stepwise regression, SS incremental
forward stagewise regression, SS least angle regression (LARS), and SS
lasso models.  All area-level covariates are considered at all available
scales to enter a model, but the SS algorithms are constrained to select
each area-level covariate at a single spatial scale.

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
