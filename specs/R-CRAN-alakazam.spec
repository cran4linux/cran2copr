%global __brp_check_rpaths %{nil}
%global packname  alakazam
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Immunoglobulin Clonal Lineage and Diversity Analysis

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-ggplot2 >= 3.2.0
BuildRequires:    R-CRAN-igraph >= 1.0.0
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.8.3
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-graphics 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-seqinr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.2.0
Requires:         R-CRAN-igraph >= 1.0.0
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.8.3
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-ape 
Requires:         R-graphics 
Requires:         R-grid 
Requires:         R-CRAN-lazyeval 
Requires:         R-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-seqinr 
Requires:         R-stats 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-tibble 
Requires:         R-utils 

%description
Provides methods for high-throughput adaptive immune receptor repertoire
sequencing (AIRR-Seq; Rep-Seq) analysis. In particular, immunoglobulin
(Ig) sequence lineage reconstruction, lineage topology analysis, diversity
profiling, amino acid property analysis and gene usage. Citations: Gupta
and Vander Heiden, et al (2017) <doi:10.1093/bioinformatics/btv359>,
Stern, Yaari and Vander Heiden, et al (2014)
<doi:10.1126/scitranslmed.3008879>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
