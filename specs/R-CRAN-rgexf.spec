%global packname  rgexf
%global packver   0.15.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.15.3
Release:          1%{?dist}
Summary:          Build, Import and Export GEXF Graph Files

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-Rook 
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-Rook 
Requires:         R-CRAN-igraph 

%description
Create, read and write GEXF (Graph Exchange XML Format) graph files (used
in Gephi and others). Using the XML package, it allows the user to easily
build/read graph files including attributes, GEXF viz attributes (such as
color, size, and position), network dynamics (for both edges and nodes)
and edge weighting. Users can build/handle graphs element-by-element or
massively through data-frames, visualize the graph on a web browser
through "sigmajs" (a javascript library) and interact with the igraph
package.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/gexf-12draft-primer.pdf
%doc %{rlibdir}/%{packname}/gexf-graphs
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/sigmajs
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
