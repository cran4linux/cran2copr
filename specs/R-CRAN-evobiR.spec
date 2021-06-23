%global __brp_check_rpaths %{nil}
%global packname  evobiR
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          2%{?dist}%{?buildtag}
Summary:          Comparative and Population Genetic Analyses

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-seqinr 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-geiger 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-phytools 
Requires:         R-CRAN-seqinr 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-geiger 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-phytools 

%description
Comparative analysis of continuous traits influencing discrete states, and
utility tools to facilitate comparative analyses.  Implementations of
ABBA/BABA type statistics to test for introgression in genomic data.
Wright-Fisher, phylogenetic tree, and statistical distribution Shiny
interactive simulations for use in teaching.

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
