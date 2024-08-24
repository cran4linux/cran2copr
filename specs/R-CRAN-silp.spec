%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  silp
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Conditional Process Analysis (CPA) via Structural Equation Modeling (SEM) Approach

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-semTools 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-semTools 
Requires:         R-stats 
Requires:         R-CRAN-stringr 

%description
Provides Reliability-Adjusted Product Indicator (RAPI) method to estimate
effects among latent variables, thus allowing for more precise definition
and analysis of mediation and moderation models. Our simulation studies
reveal that while 'silp' may exhibit instability with smaller sample sizes
and lower reliability scores (e.g., N = 100, omega = 0.7), implementing
nearest positive definite matrix correction and bootstrap confidence
interval estimation can significantly ameliorate this volatility. When
these adjustments are applied, 'silp' achieves estimations akin in quality
to those derived from latent moderated structural equations (LMS). In
conclusion, the 'silp' package is a valuable tool for researchers seeking
to explore complex relational structures between variables without
resorting to commercial software. Hsiao et
al.(2018)<doi:10.1177/0013164416679877> Kline &
Moosbrugger(2000)<doi:10.1007/BF02296338> Cheung et
al.(2021)<doi:10.1007/s10869-020-09717-0>.

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
