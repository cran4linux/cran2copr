%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DBCVindex
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Calculates the Density-Based Clustering Validation Index (DBCV) Index

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pacman 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-stats 
Requires:         R-CRAN-pacman 
Requires:         R-CRAN-Matrix 
Requires:         R-stats 

%description
A metric called 'Density-Based Clustering Validation index' (DBCV) index
to evaluate clustering results, following the
<https://github.com/FelSiq/DBCV> 'Python' implementation by Felipe Alves
Siqueira. Original 'DBCV' index article: Moulavi, D., Jaskowiak, P. A.,
Campello, R. J., Zimek, A., & Sander, J. (2014, April). "Density-based
clustering validation", Proceedings of SDM 2014 -- the 2014 SIAM
International Conference on Data Mining (pp. 839-847),
<doi:10.1137/1.9781611973440.96>.

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
