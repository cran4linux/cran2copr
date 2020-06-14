%global packname  geneListPie
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          Profiling a gene list into GOslim or KEGG function pie

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch

%description
"geneListPie" package is for mapping a gene list to function categories
defined in GOSlim or Kegg. The results can be plotted as a pie chart to
provide a quick view of the genes distribution of the gene list among the
function categories. The gene list must contain a list of gene symbols.
The package contains a set of pre-processed gene sets obtained from Gene
Ontology and MSigDB including human, mouse, rat and yeast. To provide a
high level concise view, only GO slim and kegg are provided. The gene sets
are regulared updated. User can also use customized gene sets. User can
use the R Pie() or Pie3D() function for plotting the pie chart. Users can
also choose to output the gene function mapping results and use external
software such as Excel(R) for ploting.

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
%{rlibdir}/%{packname}/INDEX
