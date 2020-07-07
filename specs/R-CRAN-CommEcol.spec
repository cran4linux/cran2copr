%global packname  CommEcol
%global packver   1.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.0
Release:          3%{?dist}
Summary:          Community Ecology Analyses

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-picante 
BuildRequires:    R-CRAN-adespatial 
BuildRequires:    R-CRAN-betapart 
BuildRequires:    R-CRAN-gmp 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-picante 
Requires:         R-CRAN-adespatial 
Requires:         R-CRAN-betapart 
Requires:         R-CRAN-gmp 

%description
Autosimilarity curves, standardization of spatial extent, dissimilarity
indexes that overweight rare species, phylogenetic and functional
(pairwise and multisample) dissimilarity indexes and nestedness for
phylogenetic, functional and other diversity metrics. This should be a
complement to available packages, particularly 'vegan'.

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
