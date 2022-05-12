%global __brp_check_rpaths %{nil}
%global packname  MixGHD
%global packver   2.3.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.7
Release:          1%{?dist}%{?buildtag}
Summary:          Model Based Clustering, Classification and Discriminant Analysis Using the Mixture of Generalized Hyperbolic Distributions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.3
Requires:         R-core >= 3.1.3
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Bessel 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-ghyp 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-mixture 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-methods 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Bessel 
Requires:         R-stats 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-ghyp 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-mixture 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-cluster 
Requires:         R-methods 

%description
Carries out model-based clustering, classification and discriminant
analysis using five different models. The models are all based on the
generalized hyperbolic distribution. The first model 'MGHD' (Browne and
McNicholas (2015) <doi:10.1002/cjs.11246>) is the classical mixture of
generalized hyperbolic distributions. The 'MGHFA' (Tortora et al. (2016)
<doi:10.1007/s11634-015-0204-z>) is the mixture of generalized hyperbolic
factor analyzers for high dimensional data sets. The 'MSGHD' is the
mixture of multiple scaled generalized hyperbolic distributions, the
'cMSGHD' is a 'MSGHD' with convex contour plots and the 'MCGHD', mixture
of coalesced generalized hyperbolic distributions is a new more flexible
model (Tortora et al. (2019)<doi:10.1007/s00357-019-09319-3>. The paper
related to the software can be found at <doi:10.18637/jss.v098.i03>.

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
