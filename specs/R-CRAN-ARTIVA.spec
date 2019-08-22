%global packname  ARTIVA
%global packver   1.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.3
Release:          1%{?dist}
Summary:          Time-Varying DBN Inference with the ARTIVA (Auto Regressive TImeVArying) Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-gplots 
Requires:         R-MASS 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-gplots 

%description
Reversible Jump MCMC (RJ-MCMC)sampling for approximating the posterior
distribution of a time varying regulatory network, under the Auto
Regressive TIme VArying (ARTIVA) model (for a detailed description of the
algorithm, see Lebre et al. BMC Systems Biology, 2010). Starting from
time-course gene expression measurements for a gene of interest (referred
to as "target gene") and a set of genes (referred to as "parent genes")
which may explain the expression of the target gene, the ARTIVA procedure
identifies temporal segments for which a set of interactions occur between
the "parent genes" and the "target gene". The time points that delimit the
different temporal segments are referred to as changepoints (CP).

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
