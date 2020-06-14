%global packname  lmmen
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          Linear Mixed Model Elastic Net

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.2
Requires:         R-core >= 3.3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-lmmlasso 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-glmmLasso 
Requires:         R-CRAN-lmmlasso 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-lme4 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-glmmLasso 

%description
Fits (Gaussian) linear mixed-effects models for high-dimensional data
(n<<p) using the linear mixed model elastic-net penalty.

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
