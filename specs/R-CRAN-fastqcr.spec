%global __brp_check_rpaths %{nil}
%global packname  fastqcr
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Quality Control of Sequencing Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-rmarkdown >= 1.4
BuildRequires:    R-CRAN-readr >= 1.3.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-rmarkdown >= 1.4
Requires:         R-CRAN-readr >= 1.3.0
Requires:         R-CRAN-dplyr 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-xml2 

%description
'FASTQC' is the most widely used tool for evaluating the quality of high
throughput sequencing data. It produces, for each sample, an html report
and a compressed file containing the raw data. If you have hundreds of
samples, you are not going to open up each 'HTML' page. You need some way
of looking at these data in aggregate. 'fastqcr' Provides helper functions
to easily parse, aggregate and analyze 'FastQC' reports for large numbers
of samples. It provides a convenient solution for building a 'Multi-QC'
report, as well as, a 'one-sample' report with result interpretations.

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
%doc %{rlibdir}/%{packname}/fastqc_results
%doc %{rlibdir}/%{packname}/report_templates
%{rlibdir}/%{packname}/INDEX
