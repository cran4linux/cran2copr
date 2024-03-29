%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SpatialKWD
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial KWD for Large Spatial Maps

License:          EUPL (>= 1.2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 

%description
Contains efficient implementations of Discrete Optimal Transport
algorithms for the computation of Kantorovich-Wasserstein distances
between pairs of large spatial maps (Bassetti, Gualandi, Veneroni (2020),
<doi:10.1137/19M1261195>). All the algorithms are based on an ad-hoc
implementation of the Network Simplex algorithm. The package has four main
helper functions: compareOneToOne() (to compare two spatial maps),
compareOneToMany() (to compare a reference map with a list of other maps),
compareAll() (to compute a matrix of distances between a list of maps),
and focusArea() (to compute the KWD distance within a focus area). In
non-convex maps, the helper functions first build the convex-hull of the
input bins and pad the weights with zeros.

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
