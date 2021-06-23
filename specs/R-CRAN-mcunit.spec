%global __brp_check_rpaths %{nil}
%global packname  mcunit
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Unit Tests for MC Methods

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-simctest >= 2.6
BuildRequires:    R-CRAN-testthat >= 2.3
BuildRequires:    R-CRAN-Rdpack >= 0.7
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-methods 
Requires:         R-CRAN-simctest >= 2.6
Requires:         R-CRAN-testthat >= 2.3
Requires:         R-CRAN-Rdpack >= 0.7
Requires:         R-stats 
Requires:         R-CRAN-rlang 
Requires:         R-methods 

%description
Unit testing for Monte Carlo methods, particularly Markov Chain Monte
Carlo (MCMC) methods, are implemented as extensions of the 'testthat'
package. The MCMC methods check whether the MCMC chain has the correct
invariant distribution. They do not check other properties of successful
samplers such as whether the chain can reach all points, i.e. whether is
recurrent. The tests require the ability to sample from the prior and to
run steps of the MCMC chain. The methodology is described in Gandy and
Scott (2020) <arXiv:2001.06465>.

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
