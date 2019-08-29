%global packname  adiv
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Analysis of Diversity

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-CRAN-adegraphics 
BuildRequires:    R-CRAN-adephylo 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-phylobase 
BuildRequires:    R-cluster 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rgl 
Requires:         R-CRAN-ade4 
Requires:         R-CRAN-adegraphics 
Requires:         R-CRAN-adephylo 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-phylobase 
Requires:         R-cluster 
Requires:         R-methods 
Requires:         R-CRAN-rgl 

%description
Includes functions, data sets and examples for the calculation of various
indices of biodiversity including species, functional and phylogenetic
diversity. Part of the indices are expressed in terms of equivalent
numbers of species. It also provides ways to partition biodiversity across
spatial or temporal scales (alpha, beta, gamma diversities). In addition
to the quantification of biodiversity, ordination approaches are available
which rely on diversity indices and allow the detailed identification of
species, functional or phylogenetic differences between communities.

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
