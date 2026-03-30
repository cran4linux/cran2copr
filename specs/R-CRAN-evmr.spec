%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  evmr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Extreme Value Modeling for r-Largest Order Statistics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-eva 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-lmomco 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-stats 
Requires:         R-CRAN-eva 
Requires:         R-graphics 
Requires:         R-CRAN-lmomco 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-Rsolnp 
Requires:         R-stats 

%description
Tools for extreme value modeling based on the r-largest order statistics
framework. The package provides functions for parameter estimation via
maximum likelihood, return level estimation with standard errors, profile
likelihood-based confidence intervals, random sample generation, and
entropy difference tests for selecting the number of order statistics r.
Several r-largest order statistics models are implemented, including the
four-parameter kappa (rK4D), generalized logistic (rGLO), generalized
Gumbel (rGGD), logistic (rLD), and Gumbel (rGD) distributions. The rK4D
methodology is described in Shin et al. (2022)
<doi:10.1016/j.wace.2022.100533>, the rGLO model in Shin and Park (2024)
<doi:10.1007/s00477-023-02642-7>, and the rGGD model in Shin and Park
(2025) <doi:10.1038/s41598-024-83273-y>. The underlying distributions are
related to the kappa distribution of Hosking (1994)
<doi:10.1017/CBO9780511529443>, the generalized logistic distribution
discussed by Ahmad et al. (1988) <doi:10.1016/0022-1694(88)90015-7>, and
the generalized Gumbel distribution of Jeong et al. (2014)
<doi:10.1007/s00477-014-0865-8>. Penalized likelihood approaches for
extreme value estimation follow Martins and Stedinger (2000)
<doi:10.1029/1999WR900330> and Coles and Dixon (1999)
<doi:10.1023/A:1009905222644>. Selection of r is supported using methods
discussed in Bader et al. (2017) <doi:10.1007/s11222-016-9697-3>. The
package is intended for hydrological, climatological, and environmental
extreme value analysis.

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
