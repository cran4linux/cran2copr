%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cxreg
%global packver   1.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Complex-Valued Lasso and Complex-Valued Graphical Lasso

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-gdata 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-gdata 
Requires:         R-grDevices 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-mvtnorm 
Requires:         R-stats 
Requires:         R-utils 

%description
Implements 'glmnet'-style complex-valued lasso (CLASSO) and complex-valued
graphical lasso (CGLASSO) via a pathwise coordinate descent algorithm for
complex-valued parameters, using an isomorphism between complex numbers
and 2x2 orthogonal matrices. Also provides a full inference pipeline for
high-dimensional sparse spectral precision matrices, including data-driven
bandwidth selection, one-step debiasing, asymptotic variance estimation,
entry-wise confidence regions, and FDR-controlled hypothesis testing.
Supporting tools for cross-validation, simulation, coefficient extraction,
and plotting are included. See Deb, Kuceyeski, and Basu (2024)
<doi:10.48550/arXiv.2401.11128> and Deb, Kim, and Basu (2026)
<doi:10.48550/arXiv.2606.07986>.

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
