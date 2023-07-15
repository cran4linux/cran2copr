%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  midas2
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Platform Design with Subgroup Efficacy Exploration(MIDAS-2)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-R2jags 
BuildRequires:    R-stats 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-R2jags 
Requires:         R-stats 

%description
The rapid screening of effective and optimal therapies from large numbers
of candidate combinations, as well as exploring subgroup efficacy, remains
challenging, which necessitates innovative, integrated, and efficient
trial designs(Yuan, Y., et al. (2016) <doi:10.1002/sim.6971>). MIDAS-2
package enables quick and continuous screening of promising combination
strategies and exploration of their subgroup effects within a unified
platform design framework. We used a regression model to characterize the
efficacy pattern in subgroups. Information borrowing was applied through
Bayesian hierarchical model to improve trial efficiency considering the
limited sample size in subgroups(Cunanan, K. M., et al. (2019)
<doi:10.1177/1740774518812779>). MIDAS-2 provides an adaptive drug
screening and subgroup exploring framework to accelerate immunotherapy
development in an efficient, accurate, and integrated fashion(Wathen, J.
K., & Thall, P. F. (2017) <doi: 10.1177/1740774517692302>).

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
