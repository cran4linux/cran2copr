%global packname  SemiParSampleSel
%global packver   1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5
Release:          1%{?dist}
Summary:          Semi-Parametric Sample Selection Modelling with Continuous orDiscrete Response

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildArch:        noarch
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-gamlss.dist 
BuildRequires:    R-CRAN-magic 
BuildRequires:    R-CRAN-trust 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-Matrix 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-CDVine 
BuildRequires:    R-CRAN-matrixStats 
Requires:         R-CRAN-copula 
Requires:         R-mgcv 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-gamlss.dist 
Requires:         R-CRAN-magic 
Requires:         R-CRAN-trust 
Requires:         R-CRAN-VGAM 
Requires:         R-Matrix 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-CDVine 
Requires:         R-CRAN-matrixStats 

%description
Routine for fitting continuous or discrete response copula sample
selection models with semi-parametric predictors, including linear and
nonlinear effects.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
