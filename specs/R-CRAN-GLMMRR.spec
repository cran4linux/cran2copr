%global packname  GLMMRR
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}
Summary:          Generalized Linear Mixed Model (GLMM) for Binary RandomizedResponse Data

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-methods 
BuildRequires:    R-lattice 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-lme4 
Requires:         R-methods 
Requires:         R-lattice 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grDevices 

%description
Generalized Linear Mixed Model (GLMM) for Binary Randomized Response Data.
Includes Cauchit, Compl. Log-Log, Logistic, and Probit link functions for
Bernoulli Distributed RR data. RR Designs: Warner, Forced Response,
Unrelated Question, Kuk, Crosswise, and Triangular.

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
