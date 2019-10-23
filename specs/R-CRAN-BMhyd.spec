%global packname  BMhyd
%global packver   1.2-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.8
Release:          1%{?dist}
Summary:          PCM for Hybridization

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-geiger 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-TreeSim 
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-CRAN-phylobase 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-geiger 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-TreeSim 
Requires:         R-CRAN-phytools 
Requires:         R-CRAN-phylobase 
Requires:         R-CRAN-mvtnorm 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats 

%description
The BMhyd package analyzes the phenotypic evolution of species of hybrid
origin on a phylogenetic network. This package can detect the hybrid vigor
effect, a burst of variation at formation, and the relative portion of
heritability from its parents. Parameters are estimated by maximum
likelihood. Users need to enter a comparative data set, a phylogeny, and
information on gene flow leading to hybrids.

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
