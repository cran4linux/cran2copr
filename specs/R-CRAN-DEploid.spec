%global packname  DEploid
%global packver   0.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.2
Release:          1%{?dist}
Summary:          Deconvolute Mixed Genomes with Unknown Proportions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-plotly >= 4.7.1
BuildRequires:    R-CRAN-rmarkdown >= 1.6
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-htmlwidgets >= 1.0
BuildRequires:    R-CRAN-scales >= 0.4.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.2
Requires:         R-CRAN-plotly >= 4.7.1
Requires:         R-CRAN-rmarkdown >= 1.6
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-htmlwidgets >= 1.0
Requires:         R-CRAN-scales >= 0.4.0
Requires:         R-CRAN-Rcpp >= 0.11.2

%description
Traditional phasing programs are limited to diploid organisms. Our method
modifies Li and Stephens algorithm with Markov chain Monte Carlo (MCMC)
approaches, and builds a generic framework that allows haplotype searches
in a multiple infection setting. This package is primarily developed as
part of the Pf3k project, which is a global collaboration using the latest
sequencing technologies to provide a high-resolution view of natural
variation in the malaria parasite Plasmodium falciparum. Parasite DNA are
extracted from patient blood sample, which often contains more than one
parasite strain, with unknown proportions. This package is used for
deconvoluting mixed haplotypes, and reporting the mixture proportions from
each sample.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
