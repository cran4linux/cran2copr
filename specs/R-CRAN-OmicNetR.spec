%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  OmicNetR
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Network-Based Integration of Multi-Omics Data Using Sparse CCA

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-igraph 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-igraph 

%description
Provides an end-to-end workflow for integrative analysis of two omics
layers using sparse canonical correlation analysis (sCCA), including
sample alignment, feature selection, network edge construction, and
visualization of gene-metabolite relationships. The underlying methods are
based on penalized matrix decomposition and sparse CCA (Witten, Tibshirani
and Hastie (2009) <doi:10.1093/biostatistics/kxp008>), with design
principles inspired by multivariate integrative frameworks such as
mixOmics (Rohart et al. (2017) <doi:10.1371/journal.pcbi.1005752>).

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
