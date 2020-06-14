%global packname  survidm
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          2%{?dist}
Summary:          Inference and Prediction in an Illness-Death Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-KernSmooth 
BuildRequires:    R-CRAN-np 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-TPmsm 
Requires:         R-KernSmooth 
Requires:         R-CRAN-np 
Requires:         R-survival 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 
Requires:         R-CRAN-doRNG 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-TPmsm 

%description
Newly developed methods for the estimation of several probabilities in an
illness-death model. The package can be used to obtain nonparametric and
semiparametric estimates for: transition probabilities, occupation
probabilities, cumulative incidence function and the sojourn time
distributions. Additionally, it is possible to fit proportional hazards
regression models in each transition of the Illness-Death Model. Several
auxiliary functions are also provided which can be used for marginal
estimation of the survival functions.

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
%{rlibdir}/%{packname}/libs
