%global packname  MplusAutomation
%global packver   0.7-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.3
Release:          3%{?dist}
Summary:          An R Package for Facilitating Large-Scale Latent VariableAnalyses in Mplus

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-gsubfn 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-texreg 
BuildRequires:    R-CRAN-pander 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-rlang 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-boot 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-gsubfn 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-xtable 
Requires:         R-lattice 
Requires:         R-CRAN-texreg 
Requires:         R-CRAN-pander 
Requires:         R-CRAN-digest 
Requires:         R-parallel 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-rlang 

%description
Leverages the R language to automate latent variable model estimation and
interpretation using 'Mplus', a powerful latent variable modeling program
developed by Muthen and Muthen (<http://www.statmodel.com>). Specifically,
this package provides routines for creating related groups of models,
running batches of models, and extracting and tabulating model parameters
and fit statistics.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
