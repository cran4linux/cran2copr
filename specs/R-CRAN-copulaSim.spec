%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  copulaSim
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Virtual Patient Simulation by Copula Invariance Property

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-mvtnorm >= 1.0.12
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-mvtnorm >= 1.0.12
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-utils 

%description
To optimize clinical trial designs and data analysis methods consistently
through trial simulation, we need to simulate multivariate mixed-type
virtual patient data independent of designs and analysis methods under
evaluation. To make the outcome of optimization more realistic, relevant
empirical patient level data should be utilized when it’s available.
However, a few problems arise in simulating trials based on small
empirical data, where the underlying marginal distributions and their
dependence structure cannot be understood or verified thoroughly due to
the limited sample size. To resolve this issue, we use the copula
invariance property, which can generate the joint distribution without
making a strong parametric assumption. The function copula.sim can
generate virtual patient data with optional data validation methods that
are based on energy distance and ball divergence measurement. The function
compare.copula.sim can conduct comparison of marginal mean and covariance
of simulated data. To simulate patient-level data from a hypothetical
treatment arm that would perform differently from the observed data, the
function new.arm.copula.sim can be used to generate new multivariate data
with the same dependence structure of the original data but with a shifted
mean vector.

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
