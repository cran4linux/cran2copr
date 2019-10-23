%global packname  RWBP
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Detects spatial outliers using a Random Walk on Bipartite Graph

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-lsa 
BuildRequires:    R-CRAN-SnowballC 
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-lsa 
Requires:         R-CRAN-SnowballC 

%description
a Bipartite graph and is constructed based on the spatial and/or
non-spatial attributes of the spatial objects in the dataset. Secondly, RW
techniques are utilized on the graphs to compute the outlierness for each
point (the differences between spatial objects and their spatial
neighbours). The top k objects with higher outlierness are recognized as
outliers.

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
%{rlibdir}/%{packname}/INDEX
