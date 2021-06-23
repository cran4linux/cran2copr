%global __brp_check_rpaths %{nil}
%global packname  ecoCopula
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Graphical Modelling and Ordination using Copulas

License:          LGPL (>= 2.1)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mvabund 
BuildRequires:    R-CRAN-glasso 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-sna 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-tweedie 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-betareg 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-glm2 
BuildRequires:    R-CRAN-ordinal 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-stats 
Requires:         R-CRAN-mvabund 
Requires:         R-CRAN-glasso 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-sna 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-tweedie 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-betareg 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-glm2 
Requires:         R-CRAN-ordinal 
Requires:         R-CRAN-foreach 
Requires:         R-stats 

%description
Creates 'graphs' of species associations (interactions) and ordination
biplots from co-occurrence data by fitting discrete gaussian copula
graphical models. Methods described in Popovic, GC., Hui, FKC., Warton,
DI., (2018) <doi:10.1016/j.jmva.2017.12.002>.

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
