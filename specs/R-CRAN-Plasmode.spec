%global packname  Plasmode
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          'Plasmode' Simulation

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-nlme >= 3.1.128
BuildRequires:    R-survival >= 2.40.1
BuildRequires:    R-mgcv >= 1.8.12
BuildRequires:    R-CRAN-glm2 >= 1.1.2
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-arm 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-twang 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-lattice 
BuildRequires:    R-splines 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-grid 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-epiDisplay 
BuildRequires:    R-foreign 
BuildRequires:    R-nnet 
Requires:         R-nlme >= 3.1.128
Requires:         R-survival >= 2.40.1
Requires:         R-mgcv >= 1.8.12
Requires:         R-CRAN-glm2 >= 1.1.2
Requires:         R-MASS 
Requires:         R-CRAN-arm 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-twang 
Requires:         R-CRAN-gbm 
Requires:         R-lattice 
Requires:         R-splines 
Requires:         R-parallel 
Requires:         R-CRAN-survey 
Requires:         R-grid 
Requires:         R-Matrix 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-latticeExtra 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-epiDisplay 
Requires:         R-foreign 
Requires:         R-nnet 

%description
Creates realistic simulated datasets for causal inference based on a
user-supplied example study, Franklin JM, Schneeweiss S, Polinski JM, and
Rassen JA (2014) <doi:10.1016/j.csda.2013.10.018>. It samples units from
the data with replacement, and then simulates the exposure, the outcome,
or both, based on the observed covariate values in the real data.

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
