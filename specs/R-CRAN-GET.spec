%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GET
%global packver   1.0-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Global Envelopes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-viridisLite 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-viridisLite 

%description
Implementation of global envelopes for a set of general d-dimensional
vectors T in various applications. A 100(1-alpha)%% global envelope is a
band bounded by two vectors such that the probability that T falls outside
this envelope in any of the d points is equal to alpha. Global means that
the probability is controlled simultaneously for all the d elements of the
vectors. The global envelopes can be used for graphical Monte Carlo and
permutation tests where the test statistic is a multivariate vector or
function (e.g. goodness-of-fit testing for point patterns and random sets,
functional analysis of variance, functional general linear model, n-sample
test of correspondence of distribution functions), for central regions of
functional or multivariate data (e.g. outlier detection, functional
boxplot) and for global confidence and prediction bands (e.g. confidence
band in polynomial regression, Bayesian posterior prediction). See
Myllymäki and Mrkvička (2023) <doi:10.48550/arXiv.1911.06583>, Myllymäki
et al. (2017) <doi:10.1111/rssb.12172>, Mrkvička and Myllymäki (2023)
<doi:10.1007/s11222-023-10275-7>, Mrkvička et al. (2016)
<doi:10.1016/j.spasta.2016.04.005>, Mrkvička et al. (2017)
<doi:10.1007/s11222-016-9683-9>, Mrkvička et al. (2020)
<doi:10.14736/kyb-2020-3-0432>, Mrkvička et al. (2021)
<doi:10.1007/s11009-019-09756-y>, Myllymäki et al. (2021)
<doi:10.1016/j.spasta.2020.100436>, Mrkvička et al. (2022)
<doi:10.1002/sim.9236>, Dai et al. (2022) <doi:10.5772/intechopen.100124>,
Dvořák and Mrkvička (2022) <doi:10.1007/s00180-021-01134-y>, Mrkvička et
al. (2023) <doi:10.48550/arXiv.2309.04746>, and Konstantinou et al. (2024)
<doi: 10.48550/arXiv.2403.01838>.

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
