%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  safestats
%global packver   0.8.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.8
Release:          1%{?dist}%{?buildtag}
Summary:          Safe Anytime-Valid Inference

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.5
Requires:         R-core >= 4.5
BuildArch:        noarch
BuildRequires:    R-graphics >= 4.2.2
BuildRequires:    R-stats >= 3.6
BuildRequires:    R-CRAN-survival >= 3.2.13
BuildRequires:    R-CRAN-lamW >= 2.2.1
BuildRequires:    R-CRAN-Matrix >= 1.7.3
BuildRequires:    R-CRAN-boot >= 1.3.28
BuildRequires:    R-CRAN-hypergeo >= 1.2.13
BuildRequires:    R-CRAN-BiasedUrn >= 1.07
BuildRequires:    R-CRAN-dplyr >= 1.0.6
BuildRequires:    R-CRAN-rlang >= 1.0.6
BuildRequires:    R-CRAN-purrr >= 0.3.5
Requires:         R-graphics >= 4.2.2
Requires:         R-stats >= 3.6
Requires:         R-CRAN-survival >= 3.2.13
Requires:         R-CRAN-lamW >= 2.2.1
Requires:         R-CRAN-Matrix >= 1.7.3
Requires:         R-CRAN-boot >= 1.3.28
Requires:         R-CRAN-hypergeo >= 1.2.13
Requires:         R-CRAN-BiasedUrn >= 1.07
Requires:         R-CRAN-dplyr >= 1.0.6
Requires:         R-CRAN-rlang >= 1.0.6
Requires:         R-CRAN-purrr >= 0.3.5

%description
Functions to design and apply tests that are anytime valid. The functions
can be used to design hypothesis tests in the prospective/randomised
control trial setting or in the observational/retrospective setting. The
resulting tests remain valid under both optional stopping and optional
continuation. The current version includes safe t-tests and safe tests of
two proportions. For details on the theory of safe tests, see Ly, A,
Boehm, Grunwald, Ramdas and van Ravenzwaaij (2024). "Safe Anytime-Valid
Inference: Practical maximally flexible sampling designs for experiments
based on e-values" (<doi:10.31234/osf.io/h5vae>) and Grunwald, de Heide
and Koolen (2024) "Safe Testing" (<doi:10.1093/jrsssb/qkae011>), for
details on safe logrank tests see ter Schure, Perez-Ortiz, Ly and Grunwald
(2024) "The Anytime-Valid Logrank Test: Error Control under Continuous
Monitoring with Unlimited Horizon" (<doi:10.51387/24-NEJSDS65>), and
Turner, Ly and Grunwald (2024) "Generic E-variables for exact sequential
k-sample tests that allow for optional stopping"
(<doi:10.1016/j.jspi.2023.106116>) for details on safe contingency table
tests.

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
