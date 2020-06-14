%global packname  VertexSort
%global packver   0.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          2%{?dist}
Summary:          Network Hierarchical Structure and Randomization

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.2
Requires:         R-core >= 3.3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-snowfall 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-snowfall 

%description
Permits to apply the 'Vertex Sort' algorithm (Jothi et al. (2009)
<10.1038/msb.2009.52>) to a graph in order to elucidate its hierarchical
structure. It also allows graphic visualization of the sorted graph by
exporting the results to a cytoscape friendly format. Moreover, it offers
five different algorithms of graph randomization: 1) Randomize a graph
with preserving node degrees, 2) with preserving similar node degrees, 3)
without preserving node degrees, 4) with preserving node in-degrees and 5)
with preserving node out-degrees.

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
