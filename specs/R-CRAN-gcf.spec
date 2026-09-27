%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gcf
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Covariate Field

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-geocomplexity 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-geocomplexity 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-spdep 
Requires:         R-stats 
Requires:         R-utils 

%description
Generates generalized covariate field (GCF) variables from spatial
covariates observed at projected coordinates, and selects a stable subset
of them for geospatial prediction. For each input covariate the method
builds spatial-pattern features (local indicator of spatial association,
local Geary's c, log local variance, rank quantile entropy, geocomplexity,
log scale variance, local variogram exponent, and signed z-score and
median absolute deviation outlier strengths over a series of buffer radii)
and neighbourhood-distribution features (buffer-wise quantiles of the
covariate values surrounding each location), reduces the buffer and
quantile sweeps to a compact set of interpretable functional summaries,
and selects variables by random forest importance combined with
spatial-block stability resampling and group voting. The GCF method is
positioned as prediction-oriented feature construction: its output feeds
any downstream regression learner. Methods are described in Song (2026)
<doi:10.1080/13658816.2026.2729719>.

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
