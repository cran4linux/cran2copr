%global packname  linkcomm
%global packver   1.0-11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.11
Release:          1%{?dist}
Summary:          Tools for Generating, Visualizing, and Analysing LinkCommunities in Networks

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-dynamicTreeCut 
BuildRequires:    R-grid 
BuildRequires:    R-utils 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-dynamicTreeCut 
Requires:         R-grid 
Requires:         R-utils 

%description
Link communities reveal the nested and overlapping structure in networks,
and uncover the key nodes that form connections to multiple communities.
linkcomm provides a set of tools for generating, visualizing, and
analysing link communities in networks of arbitrary size and type. The
linkcomm package also includes tools for generating, visualizing, and
analysing Overlapping Cluster Generator (OCG) communities.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
