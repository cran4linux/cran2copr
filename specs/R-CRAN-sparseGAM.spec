%global packname  sparseGAM
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Sparse Generalized Additive Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-grpreg 
Requires:         R-stats 
Requires:         R-splines 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-grpreg 

%description
Fits sparse frequentist GAMs (SF-GAM) for continuous and discrete
responses in the exponential dispersion family with the group lasso, group
smoothly clipped absolute deviation (SCAD), and group minimax concave
(MCP) penalties <doi:10.1007/s11222-013-9424-2>. Also fits sparse Bayesian
generalized additive models (SB-GAM) with the spike-and-slab group lasso
(SSGL) penalty of Bai et al. (2021) <doi:10.1080/01621459.2020.1765784>.
B-spline basis functions are used to model the sparse additive functions.
Stand-alone functions for group-regularized negative binomial regression,
group-regularized gamma regression, and group-regularized regression in
the exponential dispersion family with the SSGL penalty are also provided.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
