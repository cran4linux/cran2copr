%global packname  clordr
%global packver   1.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.0
Release:          3%{?dist}%{?buildtag}
Summary:          Composite Likelihood Inference and Diagnostics for ReplicatedSpatial Ordinal Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3.45
BuildRequires:    R-CRAN-rootSolve >= 1.7
BuildRequires:    R-CRAN-foreach >= 1.2.0
BuildRequires:    R-CRAN-tmvmixnorm >= 1.0.2
BuildRequires:    R-CRAN-doParallel >= 1.0.11
BuildRequires:    R-CRAN-pbivnorm >= 0.6.0
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ttutils 
Requires:         R-MASS >= 7.3.45
Requires:         R-CRAN-rootSolve >= 1.7
Requires:         R-CRAN-foreach >= 1.2.0
Requires:         R-CRAN-tmvmixnorm >= 1.0.2
Requires:         R-CRAN-doParallel >= 1.0.11
Requires:         R-CRAN-pbivnorm >= 0.6.0
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-ttutils 

%description
Composite likelihood parameter estimate and asymptotic covariance matrix
are calculated for the spatial ordinal data with replications, where
spatial ordinal response with covariate and both spatial exponential
covariance within subject and independent and identically distributed
measurement error.  Parameter estimation can be performed by either
solving the gradient function or maximizing composite log-likelihood.
Parametric bootstrapping is used to estimate the Godambe information
matrix and hence the asymptotic standard error and covariance matrix with
parallel processing option. Moreover, the proposed surrogate residual,
which extends the results of Liu and Zhang (2017) <doi:
10.1080/01621459.2017.1292915>, can act as a useful tool for model
diagnostics.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
