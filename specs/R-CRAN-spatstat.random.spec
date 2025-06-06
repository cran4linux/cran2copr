%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spatstat.random
%global packver   3.4-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Random Generation Functionality for the 'spatstat' Family

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-spatstat.geom >= 3.3.6
BuildRequires:    R-CRAN-spatstat.utils >= 3.1.4
BuildRequires:    R-CRAN-spatstat.data >= 3.1
BuildRequires:    R-CRAN-spatstat.univar >= 3.1
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-spatstat.geom >= 3.3.6
Requires:         R-CRAN-spatstat.utils >= 3.1.4
Requires:         R-CRAN-spatstat.data >= 3.1
Requires:         R-CRAN-spatstat.univar >= 3.1
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-grDevices 

%description
Functionality for random generation of spatial data in the 'spatstat'
family of packages. Generates random spatial patterns of points according
to many simple rules (complete spatial randomness, Poisson, binomial,
random grid, systematic, cell), randomised alteration of patterns
(thinning, random shift, jittering), simulated realisations of random
point processes including simple sequential inhibition, Matern inhibition
models, Neyman-Scott cluster processes (using direct, Brix-Kendall, or
hybrid algorithms), log-Gaussian Cox processes, product shot noise cluster
processes and Gibbs point processes (using Metropolis-Hastings
birth-death-shift algorithm, alternating Gibbs sampler, or
coupling-from-the-past perfect simulation). Also generates random spatial
patterns of line segments, random tessellations, and random images (random
noise, random mosaics). Excludes random generation on a linear network,
which is covered by the separate package 'spatstat.linnet'.

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
