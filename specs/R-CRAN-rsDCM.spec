%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rsDCM
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Robust and Sparse Dynamic Causal Modelling for Functional MRI

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides a robust and sparse method for group-level Dynamic Causal
Modelling (DCM) of functional magnetic resonance imaging (fMRI) data:
Student-t weighting of subjects for robustness, combined with a nonlocal
product-moment (pMOM) spike-and-slab prior for sparse selection of
group-level effects (<doi:10.48550/arXiv.2609.06379>). The package also
provides an R implementation of single-subject DCM for fMRI using
variational Laplace inversion (Friston et al., 2003
<doi:10.1016/S1053-8119(03)00202-7>), including the bilinear neural state
equation and the Buxton-Friston hemodynamic response model, ported from
the 'SPM25' (version 25.01.02) toolbox for 'MATLAB'.

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
