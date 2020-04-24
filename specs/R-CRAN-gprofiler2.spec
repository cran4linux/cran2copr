%global packname  gprofiler2
%global packver   0.1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.9
Release:          1%{?dist}
Summary:          Interface to the 'g:Profiler' Toolset

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-crosstalk 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-viridisLite 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-crosstalk 
Requires:         R-grDevices 
Requires:         R-CRAN-gridExtra 
Requires:         R-grid 
Requires:         R-CRAN-viridisLite 
Requires:         R-CRAN-dplyr 

%description
A toolset for functional enrichment analysis and visualization,
gene/protein/SNP identifier conversion and mapping orthologous genes
across species via 'g:Profiler' (<https://biit.cs.ut.ee/gprofiler>). The
main tools are: (1) 'g:GOSt' - functional enrichment analysis and
visualization of gene lists; (2) 'g:Convert' - gene/protein/transcript
identifier conversion across various namespaces; (3) 'g:Orth' - orthology
search across species; (4) 'g:SNPense' - mapping SNP rs identifiers to
chromosome positions, genes and variant effects This package is an R
interface corresponding to the 2019 update of 'g:Profiler' and provides
access to 'g:Profiler' for versions 'e94_eg41_p11' and higher. See the
package 'gProfileR' for accessing older versions from the 'g:Profiler'
toolset.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
