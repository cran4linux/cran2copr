%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  multiCCA
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multiple Canonical Correlation Analysis (Kernel and Functional)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-geigen 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-geigen 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 

%description
Implements methods for multiple canonical correlation analysis (CCA) for
more than two data blocks, with a focus on multivariate repeated measures
and functional data. The package provides two approaches: (i) multiple
kernel CCA, which embeds each data block into a reproducing kernel Hilbert
space to capture nonlinear dependencies, and (ii) multiple functional CCA,
which represents repeated measurements as smooth functions and performs
analysis in a Hilbert space framework. Both approaches are formulated via
covariance operators and solved as generalized eigenvalue problems with
regularization to ensure numerical stability. The methods allow estimation
of canonical variables, generalized canonical correlations, and
low-dimensional representations for exploratory analysis and visualization
of dependence structures across multiple feature sets. The implementation
follows the framework developed in Górecki, Krzyśko, Gnettner and Kokoszka
(2025) <doi:10.48550/arXiv.2510.04457>.

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
