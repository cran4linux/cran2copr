%global packname  strataG
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}
Summary:          Summaries and Population Structure Analyses of Genetic Data

License:          GNU General Public License
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-survival >= 2.40.1
BuildRequires:    R-CRAN-apex 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-adegenet 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pegas 
BuildRequires:    R-CRAN-phangorn 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyFiles 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-swfscMisc 
BuildRequires:    R-utils 
Requires:         R-survival >= 2.40.1
Requires:         R-CRAN-apex 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-adegenet 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-Hmisc 
Requires:         R-methods 
Requires:         R-CRAN-pegas 
Requires:         R-CRAN-phangorn 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyFiles 
Requires:         R-stats 
Requires:         R-CRAN-swfscMisc 
Requires:         R-utils 

%description
A toolkit for analyzing stratified population genetic data. Functions are
provided for summarizing and checking loci (haploid, diploid, and
polyploid), single stranded DNA sequences, calculating most population
subdivision metrics, and running external programs such as structure and
fastsimcoal. The package is further described in Archer et al (2016)
<doi:10.1111/1755-0998.12559>.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/shiny
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
