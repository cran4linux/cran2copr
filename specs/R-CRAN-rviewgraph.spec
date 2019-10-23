%global packname  rviewgraph
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Animated Graph Layout Viewer

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rJava 
Requires:         R-CRAN-rJava 

%description
This is an 'R' interface to Alun Thomas's 'ViewGraph' 'Java' graph viewing
program. It takes a graph specified as an incidence matrix, list of edges,
or in 'igraph' format and runs a graphical user interface that shows an
animation of a force directed algorithm positioning the vertices in two
dimensions. It works well for graphs of various structure of up to a few
thousand vertices. It's not fazed by graphs that comprise several
components. The coordinates can be read as an 'igraph' style layout matrix
at any time. The user can mess with the layout using a mouse, preferably
one with 3 buttons, and some keyed commands. The 'Java' program
'ViewGraph' is contained in Alun Thomas's 'JPSGCS' collection of 'Java'
programs for statistical genetics and computational statistics. The
homepage for 'JPSGCS' is
<http://www-genepi.med.utah.edu/~alun/software/index.html>. The
documentation page for 'ViewGraph' is at
<http://www-genepi.med.utah.edu/~alun/software/docs/ViewGraph.html>.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/java
%{rlibdir}/%{packname}/INDEX
