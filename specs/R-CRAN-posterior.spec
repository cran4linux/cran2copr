%global __brp_check_rpaths %{nil}
%global packname  posterior
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Working with Posterior Distributions

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-rlang >= 0.4.7
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-tensorA 
BuildRequires:    R-CRAN-pillar 
BuildRequires:    R-CRAN-distributional 
BuildRequires:    R-parallel 
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-rlang >= 0.4.7
Requires:         R-CRAN-abind 
Requires:         R-CRAN-checkmate 
Requires:         R-stats 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-tensorA 
Requires:         R-CRAN-pillar 
Requires:         R-CRAN-distributional 
Requires:         R-parallel 

%description
Provides useful tools for both users and developers of packages for
fitting Bayesian models or working with output from Bayesian models. The
primary goals of the package are to: (a) Efficiently convert between many
different useful formats of draws (samples) from posterior or prior
distributions. (b) Provide consistent methods for operations commonly
performed on draws, for example, subsetting, binding, or mutating draws.
(c) Provide various summaries of draws in convenient formats. (d) Provide
lightweight implementations of state of the art posterior inference
diagnostics. References: Vehtari et al. (2021) <doi:10.1214/20-BA1221>.

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
