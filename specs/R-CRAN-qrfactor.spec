%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  qrfactor
%global packver   1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Simultaneous Q-Mode and R-Mode Factor Analysis for Spatial Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-mvoutlier 
BuildRequires:    R-CRAN-pvclust 
Requires:         R-methods 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-mvoutlier 
Requires:         R-CRAN-pvclust 

%description
Performs Q-mode and R-mode factor analysis simultaneously on spatial and
non-spatial data. A single function, qrfactor(), carries out principal
component analysis, R-mode factor analysis, Q-mode factor analysis,
simultaneous R- and Q-mode factor analysis, principal coordinate analysis
and multidimensional scaling. Loadings and scores are returned from the
fitted object, and the plot() method provides annotated biplots for
combinations of eigenvectors, loadings and scores. Input may be supplied
as an 'ESRI' shapefile, a delimited text file or a data frame.

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
