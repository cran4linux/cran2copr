%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gllvmTMB
%global packver   0.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.1
Release:          1%{?dist}%{?buildtag}
Summary:          Generalised Linear Latent Variable Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-TMB >= 1.8.0
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-fmesher 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-BH 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-TMB >= 1.8.0
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-fmesher 
Requires:         R-CRAN-generics 
Requires:         R-graphics 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-tidyselect 
Requires:         R-utils 

%description
Fits multivariate generalised linear latent variable models using either
long-format data or a wide data frame. Models support several response
distributions and trait covariance structures, and can estimate
correlations, shared latent axes, and trait-specific variances. Binary
presence-absence data can be used for joint species distribution analyses.
Optional animal, phylogenetic, spatial, and kernel covariance components
are available. Estimation uses 'Template Model Builder'. Spatial effects
can use sparse Gaussian Markov random field constructions. This 0.7.1
release remains experimental: evidence for estimates is model- and
regime-specific. Broad interval coverage is not certified; a 0.94 coverage
floor is documented only for one two-sided Gaussian total-variance profile
setting.

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
