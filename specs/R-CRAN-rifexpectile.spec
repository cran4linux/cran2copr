%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rifexpectile
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Density-Free RIF Decompositions for Unconditional Expectiles

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-stats 
Requires:         R-graphics 

%description
Implements a density-free recentered influence function (RIF) regression
framework for unconditional expectiles, and embeds it in a two-sample
Oaxaca-Blinder decomposition indexed continuously by the expectile level.
Unlike quantile-based RIF decompositions, which require estimating an
inverse density term at each quantile, the expectile RIF depends only on
primitive moments of the outcome distribution and requires no density
estimation, no bandwidth selection, and no kernel smoothing. The package
provides expectile estimation by iteratively reweighted least squares,
closed-form RIF construction, two-sample composition/structure
decomposition across a grid of expectile levels, bootstrap-based
inference, and plotting methods. The underlying methodology is described
in Ndoye (2025), "Semi-Nonparametric Expectile RIF Regression for
Distributional Decomposition," presented at the 2025 World Congress of the
Econometric Society, Seoul, Korea,
<https://www.econometricsociety.org/regional-activities/conference-papers/view/282/943>.

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
