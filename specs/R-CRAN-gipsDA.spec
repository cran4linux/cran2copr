%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gipsDA
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Discriminant Analysis with Permutation-Invariant Covariance Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gips >= 1.3.0
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringi 
Requires:         R-CRAN-gips >= 1.3.0
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-CRAN-stringi 

%description
Extends classical linear and quadratic discriminant analysis by
incorporating permutation-group symmetries into covariance matrix
estimation. Methods based on the 'gips' framework identify and impose
permutation structures that regularize covariance estimates and improve
stability and interpretability for symmetric or exchangeable features. The
package provides pooled and class-specific covariance models, including
multi-class variants with shared or independently estimated symmetry
structures. The underlying methodology is described by Graczyk et al.
(2022) <doi:10.1214/22-AOS2174> and Chojecki, Morgen, and Kołodziejek
(2025) <doi:10.18637/jss.v112.i07>.

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
