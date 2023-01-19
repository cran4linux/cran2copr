%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pcaL1
%global packver   1.5.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.7
Release:          1%{?dist}%{?buildtag}
Summary:          L1-Norm PCA Methods

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    coin-or-Clp-devel
BuildRequires:    R-devel
Requires:         R-core

%description
Implementations of several methods for principal component analysis using
the L1 norm.  The package depends on COIN-OR Clp version >= 1.17.4.  The
methods implemented are PCA-L1 (Kwak 2008) <DOI:10.1109/TPAMI.2008.114>,
L1-PCA (Ke and Kanade 2003, 2005) <DOI:10.1109/CVPR.2005.309>, L1-PCA*
(Brooks, Dula, and Boone 2013) <DOI:10.1016/j.csda.2012.11.007>, L1-PCAhp
(Visentin, Prestwich and Armagan 2016) <DOI:10.1007/978-3-319-46227-1_37>,
wPCA (Park and Klabjan 2016) <DOI: 10.1109/ICDM.2016.0054>, awPCA (Park
and Klabjan 2016) <DOI: 10.1109/ICDM.2016.0054>, PCA-Lp (Kwak 2014)
<DOI:10.1109/TCYB.2013.2262936>, and SharpEl1-PCA (Brooks and Dula,
submitted).

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
