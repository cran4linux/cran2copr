%global packname  strataG
%global packver   2.4.905
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.905
Release:          2%{?dist}
Summary:          Summaries and Population Structure Analyses of Genetic Data

License:          GNU General Public License
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Hmisc >= 4.1
BuildRequires:    R-CRAN-phangorn >= 2.4.0
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-tibble >= 1.4.2
BuildRequires:    R-CRAN-swfscMisc >= 1.3
BuildRequires:    R-CRAN-data.table >= 1.11.4
BuildRequires:    R-CRAN-genepop >= 1.0.5
BuildRequires:    R-CRAN-apex >= 1.0.3
BuildRequires:    R-CRAN-tidyr >= 0.8.1
BuildRequires:    R-CRAN-dplyr >= 0.7.6
BuildRequires:    R-CRAN-rlang >= 0.3.0.1
BuildRequires:    R-CRAN-purrr >= 0.2.5
BuildRequires:    R-CRAN-pegas >= 0.11
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-adegenet 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rmetasim 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-utils 
Requires:         R-CRAN-Hmisc >= 4.1
Requires:         R-CRAN-phangorn >= 2.4.0
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-tibble >= 1.4.2
Requires:         R-CRAN-swfscMisc >= 1.3
Requires:         R-CRAN-data.table >= 1.11.4
Requires:         R-CRAN-genepop >= 1.0.5
Requires:         R-CRAN-apex >= 1.0.3
Requires:         R-CRAN-tidyr >= 0.8.1
Requires:         R-CRAN-dplyr >= 0.7.6
Requires:         R-CRAN-rlang >= 0.3.0.1
Requires:         R-CRAN-purrr >= 0.2.5
Requires:         R-CRAN-pegas >= 0.11
Requires:         R-CRAN-ape 
Requires:         R-CRAN-adegenet 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-methods 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rmetasim 
Requires:         R-stats 
Requires:         R-CRAN-stringi 
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

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/fastsimcoal2.html
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
