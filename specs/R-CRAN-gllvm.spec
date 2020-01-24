%global packname  gllvm
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}
Summary:          Generalized Linear Latent Variable Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-TMB 
BuildRequires:    R-CRAN-mvabund 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-fishMod 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-TMB 
Requires:         R-CRAN-mvabund 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-fishMod 
Requires:         R-mgcv 

%description
Analysis of multivariate data using generalized linear latent variable
models (gllvm). Estimation is performed using either Laplace approximation
method or variational approximation method implemented via TMB (Kristensen
et al., (2016), <doi:10.18637/jss.v070.i05>). For details see Niku et al.
(2019) <doi:10.1371/journal.pone.0216129>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
