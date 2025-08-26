%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  guidedPLS
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Supervised Dimensional Reduction by Guided Partial Least Squares

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-irlba 
BuildRequires:    R-stats 
Requires:         R-CRAN-irlba 
Requires:         R-stats 

%description
Guided partial least squares (guided-PLS) is the combination of partial
least squares by singular value decomposition (PLS-SVD) and guided
principal component analysis (guided-PCA). This package provides
implementations of PLS-SVD, guided-PLS, and guided-PCA for supervised
dimensionality reduction. The guided-PCA function (new in v1.1.0)
automatically handles mixed data types (continuous and categorical) in the
supervision matrix and provides detailed contribution analysis for
interpretability. For the details of the methods, see the reference
section of GitHub README.md <https://github.com/rikenbit/guidedPLS>.

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
