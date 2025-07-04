%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  epm
%global packver   1.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          EcoPhyloMapper

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-terra >= 1.5.21
BuildRequires:    R-CRAN-Rcpp >= 0.12.9
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-viridisLite 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppProgress 
Requires:         R-CRAN-terra >= 1.5.21
Requires:         R-CRAN-Rcpp >= 0.12.9
Requires:         R-CRAN-sf 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-viridisLite 
Requires:         R-CRAN-pbapply 
Requires:         R-methods 
Requires:         R-CRAN-RcppProgress 

%description
Facilitates the aggregation of species' geographic ranges from vector or
raster spatial data, and that enables the calculation of various
morphological and phylogenetic community metrics across geography.
Citation: Title, PO, DL Swiderski and ML Zelditch (2022)
<doi:10.1111/2041-210X.13914>.

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
