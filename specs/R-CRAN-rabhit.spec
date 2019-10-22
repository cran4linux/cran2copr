%global packname  rabhit
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Inference Tool for Antibody Haplotype

License:          CC BY-SA 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.5
Requires:         R-core >= 3.2.5
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.7.1
BuildRequires:    R-CRAN-gtools >= 3.5.0
BuildRequires:    R-CRAN-ggplot2 >= 2.0.0
BuildRequires:    R-CRAN-dendextend >= 1.9.0
BuildRequires:    R-CRAN-cowplot >= 0.9.1
BuildRequires:    R-CRAN-dplyr >= 0.5.0
BuildRequires:    R-CRAN-tigger >= 0.2.11
BuildRequires:    R-CRAN-alakazam >= 0.2.10
BuildRequires:    R-CRAN-ggdendro >= 0.1.20
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-stringi 
Requires:         R-CRAN-plotly >= 4.7.1
Requires:         R-CRAN-gtools >= 3.5.0
Requires:         R-CRAN-ggplot2 >= 2.0.0
Requires:         R-CRAN-dendextend >= 1.9.0
Requires:         R-CRAN-cowplot >= 0.9.1
Requires:         R-CRAN-dplyr >= 0.5.0
Requires:         R-CRAN-tigger >= 0.2.11
Requires:         R-CRAN-alakazam >= 0.2.10
Requires:         R-CRAN-ggdendro >= 0.1.20
Requires:         R-CRAN-reshape2 
Requires:         R-stats 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-gridExtra 
Requires:         R-methods 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-gtable 
Requires:         R-grDevices 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-stringi 

%description
Infers V-D-J haplotypes and gene deletions from AIRR-seq data, based on
IGHJ, IGHD or IGHV as anchor, by adapting a Bayesian framework. It also
calculates a Bayes factor, a number that indicates the certainty level of
the inference, for each haplotyped gene. Citation: Gidoni, et al (2019)
<doi:10.1038/s41467-019-08489-3>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
