%global packname  rgexf
%global packver   0.16.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.16.0
Release:          3%{?dist}%{?buildtag}
Summary:          Build, Import and Export GEXF Graph Files

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-servr 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-igraph 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-CRAN-servr 

%description
Create, read and write 'GEXF' (Graph Exchange 'XML' Format) graph files
(used in 'Gephi' and others). Using the 'XML' package, it allows the user
to easily build/read graph files including attributes, 'GEXF' visual
attributes (such as color, size, and position), network dynamics (for both
edges and nodes) and edge weighting. Users can build/handle graphs
element-by-element or massively through data-frames, visualize the graph
on a web browser through 'gexf-js' (a 'javascript' library) and interact
with the 'igraph' package.

%prep
%setup -q -c -n %{packname}
sed -i '/system.file/d' %{packname}/man/plot.gexf.Rd
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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/gexf-graphs
%doc %{rlibdir}/%{packname}/gexf-js
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
