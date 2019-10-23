%global packname  starmie
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          Population Structure Model Inference and Visualisation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.1.0
BuildRequires:    R-CRAN-readr >= 1.0.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-iterpc 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-label.switching 
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-CRAN-MCL 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-ggdendro 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-parallel 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 2.1.0
Requires:         R-CRAN-readr >= 1.0.0
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-iterpc 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-label.switching 
Requires:         R-CRAN-proxy 
Requires:         R-CRAN-MCL 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-ggdendro 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-MCMCpack 
Requires:         R-parallel 
Requires:         R-methods 
Requires:         R-stats 

%description
Data structures and methods for manipulating output of genetic population
structure clustering algorithms. 'starmie' can parse output from
'STRUCTURE' (see <https://pritchardlab.stanford.edu/structure.html> for
details) or 'ADMIXTURE' (see
<https://www.genetics.ucla.edu/software/admixture/> for details).
'starmie' performs model selection via information criterion, and provides
functions for MCMC diagnostics, correcting label switching and
visualisation of admixture coefficients.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/vignette-supp
%{rlibdir}/%{packname}/INDEX
