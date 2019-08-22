%global packname  adephylo
%global packver   1.1-11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.11
Release:          1%{?dist}
Summary:          Exploratory Analyses for the Phylogenetic Comparative Method

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ade4 >= 1.7.10
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-phylobase 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-adegenet 
Requires:         R-CRAN-ade4 >= 1.7.10
Requires:         R-methods 
Requires:         R-CRAN-phylobase 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-adegenet 

%description
Multivariate tools to analyze comparative data, i.e. a phylogeny and some
traits measured for each taxa.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
