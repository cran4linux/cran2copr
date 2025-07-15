%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  thamesmix
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Truncated Harmonic Mean Estimator of the Marginal Likelihood for Mixtures

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sparsediscrim 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-gor 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-withr 
Requires:         R-stats 
Requires:         R-CRAN-sparsediscrim 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-gor 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-withr 

%description
Implements the truncated harmonic mean estimator (THAMES) of the
reciprocal marginal likelihood for uni- and multivariate mixture models
using posterior samples and unnormalized log posterior values via
reciprocal importance sampling. Metodiev, Irons, Perrot-Dockès, Latouche &
Raftery (2025) <doi:10.48550/arXiv.2504.21812>.

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
