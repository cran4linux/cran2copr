%global packname  HCD
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          3%{?dist}
Summary:          Hierarchical Community Detection by Recursive Partitioning

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-randnet 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-irlba 
BuildRequires:    R-CRAN-data.tree 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-dendextend 
Requires:         R-Matrix 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-randnet 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-irlba 
Requires:         R-CRAN-data.tree 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-dendextend 

%description
Hierarchical community detection on networks by a recursive spectral
partitioning strategy, which is shown to be effective and efficient in Li,
Lei, Bhattacharyya, Sarkar, Bickel, and Levina (2018) <arXiv:1810.01509>.
The package also includes a data generating function for a binary tree
stochastic block model, a special case of stochastic block model that
admits hierarchy between communities.

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
