%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ria.test
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Testing Equality of Natural Mediation Effects and Their Randomized Interventional Analogues

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ife >= 0.2.1
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-origami 
BuildRequires:    R-CRAN-torch 
BuildRequires:    R-CRAN-Rsymphony 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-S7 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-coro 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-mlr3superlearner 
BuildRequires:    R-CRAN-progressr 
Requires:         R-CRAN-ife >= 0.2.1
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-origami 
Requires:         R-CRAN-torch 
Requires:         R-CRAN-Rsymphony 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-S7 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-coro 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-mlr3superlearner 
Requires:         R-CRAN-progressr 

%description
Implements the empirical test introduced by Yu, Ge, and Elwert (2026) for
detecting when randomized interventional analogues should not be
interpreted as natural mediation effects. The package estimates natural
effects, their randomized interventional analogues, and TE - TE^R, the
difference between the total effect and its randomized interventional
analogue. Rejecting TE - TE^R = 0 falsifies the composite null that the
natural indirect and direct effects equal their randomized interventional
analogues. The procedure remains valid in settings where the natural
effects themselves are not identified, and |TE - TE^R| provides a lower
bound on the total divergence between the natural and randomized
interventional decompositions.

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
