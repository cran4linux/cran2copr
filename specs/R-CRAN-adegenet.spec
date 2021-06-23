%global __brp_check_rpaths %{nil}
%global packname  adegenet
%global packver   2.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.3
Release:          3%{?dist}%{?buildtag}
Summary:          Exploratory Analysis of Genetic and Genomic Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14
Requires:         R-core >= 2.14
BuildRequires:    R-CRAN-dplyr >= 0.4.1
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-seqinr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-vegan 
Requires:         R-CRAN-dplyr >= 0.4.1
Requires:         R-methods 
Requires:         R-CRAN-ade4 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-MASS 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-seqinr 
Requires:         R-parallel 
Requires:         R-CRAN-spdep 
Requires:         R-boot 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-vegan 

%description
Toolset for the exploration of genetic and genomic data. Adegenet provides
formal (S4) classes for storing and handling various genetic data,
including genetic markers with varying ploidy and hierarchical population
structure ('genind' class), alleles counts by populations ('genpop'), and
genome-wide SNP data ('genlight'). It also implements original
multivariate methods (DAPC, sPCA), graphics, statistical tests, simulation
tools, distance and similarity measures, and several spatial methods. A
range of both empirical and simulated datasets is also provided to
illustrate various methods.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/dapcServer
%doc %{rlibdir}/%{packname}/files
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
