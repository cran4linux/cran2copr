%global __brp_check_rpaths %{nil}
%global packname  FunCluster
%global packver   1.09
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.09
Release:          3%{?dist}%{?buildtag}
Summary:          Functional Profiling of Microarray Expression Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-cluster 
Requires:         R-CRAN-Hmisc 
Requires:         R-cluster 

%description
FunCluster performs a functional analysis of microarray expression data
based on Gene Ontology & KEGG functional annotations. From expression data
and functional annotations FunCluster builds classes of putatively
co-regulated biological processes through a specially designed clustering
procedure.

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
