%global packname  hierarchicalDS
%global packver   3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0
Release:          1%{?dist}
Summary:          Functions to Perform Hierarchical Analysis of Distance SamplingData

License:          Unlimited
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-mc2d 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-MCMCpack 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-mvtnorm 
Requires:         R-Matrix 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-mc2d 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-MCMCpack 

%description
Functions for performing hierarchical analysis of distance sampling data,
with ability to use an areal spatial ICAR model on top of user supplied
covariates to get at variation in abundance intensity.  The detection
model can be specified as a function of observer and individual
covariates, where a parametric model is supposed for the population level
distribution of covariate values. The model uses data augmentation and a
reversible jump MCMC algorithm to sample animals that were never observed.
Also included is the ability to include point independence (increasing
correlation multiple observer's observations as a function of distance,
with independence assumed for distance=0 or first distance bin), as well
as the ability to model species misclassification rates using a
multinomial logit formulation on data from double observers.  There is
also the the ability to include zero inflation, but this is only
recommended for cases where sample sizes and spatial coverage of the
survey are high.

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
%doc %{rlibdir}/%{packname}/cache
%doc %{rlibdir}/%{packname}/figure
%doc %{rlibdir}/%{packname}/HierarchicalDS_vignette.log
%doc %{rlibdir}/%{packname}/HierarchicalDS_vignette.pdf
%doc %{rlibdir}/%{packname}/HierarchicalDS_vignette.Rnw
%doc %{rlibdir}/%{packname}/HierarchicalDS_vignette.tex
%doc %{rlibdir}/%{packname}/HierarchicalDS_vignette.toc
%doc %{rlibdir}/%{packname}/NEWS.txt
%{rlibdir}/%{packname}/simulate_data_overd.R
%{rlibdir}/%{packname}/INDEX
