%global packname  scoper
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Spectral Clustering-Based Method for Identifying B Cell Clones

License:          CC BY-SA 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildRequires:    R-CRAN-ggplot2 >= 3.2.0
BuildRequires:    R-CRAN-dplyr >= 0.8.1
BuildRequires:    R-CRAN-alakazam >= 0.3.0
BuildRequires:    R-CRAN-shazam >= 0.2.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-seqinr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-ggplot2 >= 3.2.0
Requires:         R-CRAN-dplyr >= 0.8.1
Requires:         R-CRAN-alakazam >= 0.3.0
Requires:         R-CRAN-shazam >= 0.2.0
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-seqinr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-stringr 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-rlang 

%description
Provides a computational framework for B cell clones identification from
adaptive immune receptor repertoire sequencing (AIRR-Seq) datasets. Three
models are included (identical, hierarchical, and spectral) that perform
clustering among sequences of BCRs/IGs (B cell receptors/immunoglobulins)
which share the same V gene, J gene and junction length. Nouri N and
Kleinstein SH (2018) <doi: 10.1093/bioinformatics/bty235>. Gupta NT, et
al. (2017) <doi: 10.4049/jimmunol.1601850>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
