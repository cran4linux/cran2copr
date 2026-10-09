%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  proxymix
%global packver   0.16.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.16.0
Release:          1%{?dist}%{?buildtag}
Summary:          Kullback-Leibler Optimal Gaussian Mixture Proxies for Target Densities

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3
Requires:         R-core >= 4.3
BuildArch:        noarch
BuildRequires:    R-CRAN-S7 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mvnfast 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-S7 
Requires:         R-stats 
Requires:         R-CRAN-mvnfast 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-withr 

%description
Fits multivariate Gaussian-mixture proxies that are Kullback-Leibler
optimal to user-supplied target densities on real Euclidean space. Three
fitting regimes are unified under one verb: (i) closed-form moment
matching for a single component, (ii) classical expectation-maximisation
when independent samples are available, and (iii) importance-sampled
expectation-maximisation that minimises the Kullback-Leibler divergence
when the target can be evaluated point-wise but not (cheaply) sampled.
Closed-form Gaussian-mixture operators (density, sampling,
marginalisation, conditioning, divergence) round out the toolkit. The
conditioning operator drives multiple imputation of data missing at
random, covering the multimodal and heteroscedastic cases a
single-Gaussian model cannot represent. Implements the regime hierarchy of
van der Hoek and Elliott (2024) <doi:10.1080/07362994.2024.2372605>.

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
