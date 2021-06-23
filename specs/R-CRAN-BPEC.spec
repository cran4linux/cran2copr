%global __brp_check_rpaths %{nil}
%global packname  BPEC
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          2%{?dist}%{?buildtag}
Summary:          Bayesian Phylogeographic and Ecological Clustering

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-OpenStreetMap 
BuildRequires:    R-CRAN-ggmap 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-phytools 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-coda 
Requires:         R-methods 
Requires:         R-CRAN-OpenStreetMap 
Requires:         R-CRAN-ggmap 
Requires:         R-CRAN-ape 
Requires:         R-utils 

%description
Model-based clustering for phylogeographic data comprising mtDNA sequences
and geographical locations along with optional environmental
characteristics, aiming to identify migration events that led to
homogeneous population clusters. The package vignette, I. Manolopoulou, A.
Hille, B. C. Emerson (2020) <doi:10.18637/jss.v092.i03>, provides detailed
descriptions of the package.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
