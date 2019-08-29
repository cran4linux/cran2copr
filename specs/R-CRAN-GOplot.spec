%global packname  GOplot
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Visualization of Functional Analysis Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.0.0
BuildRequires:    R-CRAN-gridExtra >= 2.0.0
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.2
BuildRequires:    R-CRAN-ggdendro >= 0.1.17
Requires:         R-CRAN-ggplot2 >= 2.0.0
Requires:         R-CRAN-gridExtra >= 2.0.0
Requires:         R-CRAN-RColorBrewer >= 1.1.2
Requires:         R-CRAN-ggdendro >= 0.1.17

%description
Implementation of multilayered visualizations for enhanced graphical
representation of functional analysis data. It combines and integrates
omics data derived from expression and functional annotation enrichment
analyses. Its plotting functions have been developed with an hierarchical
structure in mind: starting from a general overview to identify the most
enriched categories (modified bar plot, bubble plot) to a more detailed
one displaying different types of relevant information for the molecules
in a given set of categories (circle plot, chord plot, cluster plot, Venn
diagram, heatmap).

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
