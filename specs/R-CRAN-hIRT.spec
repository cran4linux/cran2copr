%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hIRT
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Hierarchical Item Response Theory Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rms >= 5.1.1
BuildRequires:    R-CRAN-Matrix >= 1.2.10
BuildRequires:    R-CRAN-ltm >= 1.1.1
BuildRequires:    R-stats 
Requires:         R-CRAN-rms >= 5.1.1
Requires:         R-CRAN-Matrix >= 1.2.10
Requires:         R-CRAN-ltm >= 1.1.1
Requires:         R-stats 

%description
Implementation of a class of hierarchical item response theory (IRT)
models where both the mean and the variance of latent preferences (ability
parameters) may depend on observed covariates. The current implementation
includes both the two-parameter latent trait model for binary data and the
graded response model for ordinal data. Both are fitted via the
Expectation-Maximization (EM) algorithm. Asymptotic standard errors are
derived from the observed information matrix. See Zhou (2019)
<doi:10.1017/pan.2018.63> for details.

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
