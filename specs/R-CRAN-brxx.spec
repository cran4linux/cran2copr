%global __brp_check_rpaths %{nil}
%global packname  brxx
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Test Reliability Estimation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-GPArotation 
BuildRequires:    R-CRAN-TeachingDemos 
BuildRequires:    R-CRAN-blavaan 
BuildRequires:    R-CRAN-blme 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-rstan 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-GPArotation 
Requires:         R-CRAN-TeachingDemos 
Requires:         R-CRAN-blavaan 
Requires:         R-CRAN-blme 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-rstan 
Requires:         R-CRAN-rstantools

%description
When samples contain missing data, are small, or are suspected of bias,
estimation of scale reliability may not be trustworthy.  A recommended
solution for this common problem has been Bayesian model estimation.
Bayesian methods rely on user specified information from historical data
or researcher intuition to more accurately estimate the parameters.  This
package provides a user friendly interface for estimating test
reliability.  Here, reliability is modeled as a beta distributed random
variable with shape parameters alpha=true score variance and beta=error
variance (Tanzer & Harlow, 2020) <doi:10.1080/00273171.2020.1854082>.

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
