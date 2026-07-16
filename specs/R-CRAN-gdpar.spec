%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gdpar
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          General Dynamic Parameter Models via Reference Anchoring

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-posterior 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-posterior 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-withr 

%description
Implements a unified predictive framework in which individual parameters
are decomposed as theta_i equal to theta_ref plus Delta(x_i, theta_ref),
with theta_ref a population reference and Delta an explicit deviation
function. The decomposition follows the Additive-Multiplicative-Modulated
canonical form and is estimated through three complementary paths:
hierarchical Bayesian inference via 'Stan', varying-coefficient models via
penalized splines, and amortized inference via hypernetworks in 'torch'.
The package provides identifiability diagnostics, validity tests for the
population reference, and benchmarks against canonical zero-inflated count
datasets and avian abundance data from the eBird Status and Trends
project. The framework and its estimation paths are described in Gomez
Julian (2026) <doi:10.5281/zenodo.21046269>.

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
