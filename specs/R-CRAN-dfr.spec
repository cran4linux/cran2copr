%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dfr
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Dual Feature Reduction for SGL

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-sgs 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-sgs 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-Matrix 

%description
Implementation of the Dual Feature Reduction (DFR) approach for the Sparse
Group Lasso (SGL) and the Adaptive Sparse Group Lasso (aSGL) (Feser and
Evangelou (2024) <doi:10.48550/arXiv.2405.17094>). The DFR approach is a
feature reduction approach that applies strong screening to reduce the
feature space before optimisation, leading to speed-up improvements for
fitting SGL (Simon et al. (2013) <doi:10.1080/10618600.2012.681250>) and
aSGL (Mendez-Civieta et al. (2020) <doi:10.1007/s11634-020-00413-8> and
Poignard (2020) <doi:10.1007/s10463-018-0692-7>) models. DFR is
implemented using the Adaptive Three Operator Splitting (ATOS) (Pedregosa
and Gidel (2018) <doi:10.48550/arXiv.1804.02339>) algorithm, with linear
and logistic SGL models supported, both of which can be fit using k-fold
cross-validation. Dense and sparse input matrices are supported.

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
