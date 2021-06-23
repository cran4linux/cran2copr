%global __brp_check_rpaths %{nil}
%global packname  treespace
%global packver   1.1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Exploration of Landscapes of Phylogenetic Trees

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-CRAN-adegenet 
BuildRequires:    R-CRAN-adegraphics 
BuildRequires:    R-CRAN-adephylo 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-distory 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-phangorn 
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-RLumShiny 
BuildRequires:    R-CRAN-scatterD3 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyBS 
BuildRequires:    R-utils 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-ade4 
Requires:         R-CRAN-adegenet 
Requires:         R-CRAN-adegraphics 
Requires:         R-CRAN-adephylo 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-distory 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-phangorn 
Requires:         R-CRAN-phytools 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-RLumShiny 
Requires:         R-CRAN-scatterD3 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyBS 
Requires:         R-utils 

%description
Tools for the exploration of distributions of phylogenetic trees. This
package includes a 'shiny' interface which can be started from R using
treespaceServer(). For further details see Jombart et al. (2017)
<DOI:10.1111/1755-0998.12676>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
