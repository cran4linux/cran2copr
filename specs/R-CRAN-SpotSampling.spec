%global packname  SpotSampling
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          SPatial and Optimally Temporal (SPOT) Sampling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-BalancedSampling 
BuildRequires:    R-CRAN-sampling 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-WaveSampling 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-BalancedSampling 
Requires:         R-CRAN-sampling 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-WaveSampling 
Requires:         R-CRAN-MASS 

%description
In spatial data, information of two neighboring units are generally very
similar. For spatial sampling, it is therefore more efficient to select
samples that are well spread out in space. Often, the interest lies not
only in estimating a measure at one point in time, but rather in
estimating several points in time to also study the evolution. Three new
methods called Orfs (Optimal Rotation with Fixed sample Size), Orsp
(Optimal Rotation with Spread sample), and Spot (Spatial and Optimally
Temporal Sampling) are implemented in this package. Orfs allows to select
temporal samples with fixed size. Orsp selects spatio-temporal samples
with random size that are well spread out in space at each point in time.
And Spot generates spread sample with fixed sample size at each wave.
These methods provide an optimal time rotation of the selected units using
the systematic sampling.

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
