%global packname  StempCens
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Spatio-Temporal Estimation and Prediction for Censored/MissingResponses

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ssym 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-spTimer 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-tmvtnorm 
BuildRequires:    R-CRAN-MCMCglmm 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-distances 
BuildRequires:    R-CRAN-gridExtra 
Requires:         R-CRAN-ssym 
Requires:         R-CRAN-optimx 
Requires:         R-Matrix 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-spTimer 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-tmvtnorm 
Requires:         R-CRAN-MCMCglmm 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-CRAN-distances 
Requires:         R-CRAN-gridExtra 

%description
It estimates the parameters of a censored or missing data in
spatio-temporal models using the SAEM algorithm (Delyon et al., 1999
<doi:10.1214/aos/1018031103>). This algorithm is a stochastic
approximation of the widely used EM algorithm and an important tool for
models in which the E-step does not have an analytic form. Besides the
expressions obtained to estimate the parameters to the proposed model, we
include the calculations for the observed information matrix using the
method developed by Louis (1982) <https://www.jstor.org/stable/2345828>.
To examine the performance of the fitted model, case-deletion measure are
provided.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/cran-comments.md
%doc %{rlibdir}/%{packname}/cran-comments.Rmd
%{rlibdir}/%{packname}/INDEX
