%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Rtapas
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Random Tanglegram Partitions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-distory 
BuildRequires:    R-CRAN-GiniWegNeg 
BuildRequires:    R-CRAN-paco 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-parallelly 
Requires:         R-CRAN-phytools 
Requires:         R-parallel 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-distory 
Requires:         R-CRAN-GiniWegNeg 
Requires:         R-CRAN-paco 
Requires:         R-stats 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-parallelly 

%description
Applies a given global-fit method to random partial tanglegrams of a fixed
size to identify the associations, terminals, and nodes that maximize
phylogenetic (in)congruence. It also includes functions to compute more
easily the confidence intervals of classification metrics and plot
results, reducing computational time. See Llaberia-Robledillo et al.
(2022, <doi:10.1101/2022.05.17.492291>).

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
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
