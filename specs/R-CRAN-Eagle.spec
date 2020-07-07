%global packname  Eagle
%global packver   2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2
Release:          3%{?dist}
Summary:          Multiple Locus Association Mapping on a Genome-Wide Scale

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-shinyFiles 
BuildRequires:    R-CRAN-shinyBS 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggthemes 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-mmap 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-shinyFiles 
Requires:         R-CRAN-shinyBS 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggthemes 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-mmap 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-shinyjs 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-parallel 
Requires:         R-CRAN-data.table 

%description
An implementation of multiple-locus association mapping on a genome-wide
scale. 'Eagle' can handle inbred and outbred study populations,
populations of arbitrary unknown complexity, and data larger than the
memory capacity of the computer. Since 'Eagle' is based on linear mixed
models, it is best suited to the analysis of data on continuous traits.
However, it can tolerate non-normal data. 'Eagle' reports, as its
findings, the best set of snp in strongest association with a trait. For
users unfamiliar with R, to perform an analysis, run 'OpenGUI()'. This
opens a web browser to the menu-driven user interface for the input of
data, and for performing genome-wide analysis.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/shiny_app
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
