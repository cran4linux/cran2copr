%global __brp_check_rpaths %{nil}
%global packname  susieR
%global packver   0.11.84
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.11.84
Release:          1%{?dist}%{?buildtag}
Summary:          Sum of Single Effects Linear Regression

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-mixsqp 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-mixsqp 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-ggplot2 

%description
Implements methods for variable selection in linear regression based on
the "Sum of Single Effects" (SuSiE) model, as described in Wang et al
(2020) <DOI:10.1101/501114>. These methods provide simple summaries,
called "Credible Sets", for accurately quantifying uncertainty in which
variables should be selected. The methods are motivated by genetic
fine-mapping applications, and are particularly well-suited to settings
where variables are highly correlated and detectable effects are sparse.
The fitting algorithm, a Bayesian analogue of stepwise selection methods
called "Iterative Bayesian Stepwise Selection" (IBSS), is simple and fast,
allowing the SuSiE model be fit to large data sets (thousands of samples
and hundreds of thousands of variables).

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
