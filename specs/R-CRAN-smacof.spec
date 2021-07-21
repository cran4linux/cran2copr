%global __brp_check_rpaths %{nil}
%global packname  smacof
%global packver   2.1-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Multidimensional Scaling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-polynom 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-nnls 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-weights 
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-CRAN-wordcloud 
BuildRequires:    R-CRAN-candisc 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-e1071 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-polynom 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-nnls 
Requires:         R-grDevices 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-weights 
Requires:         R-CRAN-ellipse 
Requires:         R-CRAN-wordcloud 
Requires:         R-CRAN-candisc 
Requires:         R-parallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 

%description
Implements the following approaches for multidimensional scaling (MDS)
based on stress minimization using majorization (smacof):
ratio/interval/ordinal/spline MDS on symmetric dissimilarity matrices, MDS
with external constraints on the configuration, individual differences
scaling (idioscal, indscal), MDS with spherical restrictions, and
ratio/interval/ordinal/spline unfolding (circular restrictions,
row-conditional). Various tools and extensions like jackknife MDS,
bootstrap MDS, permutation tests, MDS biplots, gravity models,
unidimensional scaling, drift vectors (asymmetric MDS), classical scaling,
and Procrustes are implemented as well.

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
