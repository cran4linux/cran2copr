%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SCBiclust
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Identifies Mean, Variance, and Hierarchically Clustered Biclusters

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-sigclust 
BuildRequires:    R-CRAN-sparcl 
Requires:         R-CRAN-sigclust 
Requires:         R-CRAN-sparcl 

%description
Identifies a bicluster, a submatrix of the data such that the features and
observations within the submatrix differ from those not contained in
submatrix, using a two-step method. In the first step, observations in the
bicluster are identified to maximize the sum of weighted between cluster
feature differences. The method is described in Helgeson et al. (2020)
<doi:10.1111/biom.13136>. 'SCBiclust' can be used to identify biclusters
which differ based on feature means, feature variances, or more general
differences.

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
