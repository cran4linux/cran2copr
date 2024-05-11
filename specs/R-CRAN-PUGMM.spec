%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PUGMM
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Parsimonious Ultrametric Gaussian Mixture Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ClusterR 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-mcompanion 
BuildRequires:    R-CRAN-ppclust 
Requires:         R-CRAN-ClusterR 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-mcompanion 
Requires:         R-CRAN-ppclust 

%description
Finite Gaussian mixture models with parsimonious extended ultrametric
covariance structures estimated via a grouped coordinate ascent algorithm,
which is equivalent to the Expectation-Maximization algorithm. The
thirteen ultrametric covariance structures implemented allow for the
inspection of different hierarchical relationships among variables. The
estimation of an ultrametric correlation matrix is included as a function.
The methodologies are described in Cavicchia, Vichi, Zaccaria (2024)
<doi:10.1007/s11222-024-10405-9>, Cavicchia, Vichi, Zaccaria (2022)
<doi:10.1007/s11634-021-00488-x> and Cavicchia, Vichi, Zaccaria (2020)
<doi:10.1007/s11634-020-00400-z>.

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
