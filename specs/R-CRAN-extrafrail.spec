%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  extrafrail
%global packver   1.14
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.14
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation and Additional Tools for Alternative Shared Frailty Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-expint 
BuildRequires:    R-CRAN-msm 
Requires:         R-stats 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-expint 
Requires:         R-CRAN-msm 

%description
Provide estimation and data generation tools for new multivariate frailty
models. This version includes the gamma, inverse Gaussian, weighted
Lindley, Birnbaum-Saunders, truncated normal, mixture of inverse Gaussian,
mixture of Birnbaum-Saunders, generalized exponential and
Jorgensen-Seshadri-Whitmore as the distribution for frailty terms. For the
basal model, it is considered a parametric approach based on the
exponential, Weibull and the piecewise exponential distributions as well
as a semiparametric approach. For details, see Gallardo et al. (2024)
<doi:10.1007/s11222-024-10458-w>, Gallardo et al. (2025)
<doi:10.1002/bimj.70044>, Kiprotich et al. (2025)
<doi:10.1177/09622802251338984> and Gallardo et al. (2025)
<doi:10.1038/s41598-025-15903-y>.

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
