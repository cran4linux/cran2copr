%global packname  betapart
%global packver   1.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.1
Release:          3%{?dist}
Summary:          Partitioning Beta Diversity into Turnover and NestednessComponents

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-fastmatch 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-picante 
BuildRequires:    R-CRAN-rcdd 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-fastmatch 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-picante 
Requires:         R-CRAN-rcdd 

%description
Functions to compute pair-wise dissimilarities (distance matrices) and
multiple-site dissimilarities, separating the turnover and
nestedness-resultant components of taxonomic (incidence and abundance
based), functional and phylogenetic beta diversity.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
