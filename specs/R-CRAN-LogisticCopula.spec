%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LogisticCopula
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Copula Based Extension of Logistic Regression

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-numDeriv >= 8.1.1
BuildRequires:    R-CRAN-VineCopula >= 2.5.0
BuildRequires:    R-CRAN-igraph >= 2.0.3
BuildRequires:    R-CRAN-stringr >= 1.5.1
BuildRequires:    R-CRAN-brglm2 >= 0.9
BuildRequires:    R-CRAN-rvinecopulib >= 0.6.3.1.1
Requires:         R-CRAN-numDeriv >= 8.1.1
Requires:         R-CRAN-VineCopula >= 2.5.0
Requires:         R-CRAN-igraph >= 2.0.3
Requires:         R-CRAN-stringr >= 1.5.1
Requires:         R-CRAN-brglm2 >= 0.9
Requires:         R-CRAN-rvinecopulib >= 0.6.3.1.1

%description
An implementation of a method of extending a logistic regression model
beyond linear effects of the co-variates. The extension in is constructed
by first equating the logistic regression model to a naive Bayes model
where all the margins are specified to follow natural exponential
distributions conditional on Y, that is, a model for Y given X that is
specified through the distribution of X given Y, where the columns of X
are assumed to be mutually independent conditional on Y. Subsequently, the
model is expanded by adding vine - copulas to relax the assumption of
mutual independence, where pair-copulas are added in a stage-wise, forward
selection manner. Some heuristics are employed during the process of
selecting edges, as well as the families of pair-copula models. After each
component is added, the parameters are updated by a (smaller) number of
gradient steps to maximise the likelihood. When the algorithm has stopped
adding edges, based the criterion that a new edge should improve the
likelihood more than k times the number new parameters, the parameters are
updated with a larger number of gradient steps, or until convergence.

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
