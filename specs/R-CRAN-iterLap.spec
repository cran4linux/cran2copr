%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  iterLap
%global packver   1.1-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Approximate Probability Densities by Iterated Laplace Approximations

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15
Requires:         R-core >= 2.15
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-randtoolbox 
BuildRequires:    R-parallel 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-randtoolbox 
Requires:         R-parallel 

%description
The iterLap (iterated Laplace approximation) algorithm approximates a
general (possibly non-normalized) probability density on R^p, by repeated
Laplace approximations to the difference between current approximation and
true density (on log scale). The final approximation is a mixture of
multivariate normal distributions and might be used for example as a
proposal distribution for importance sampling (eg in Bayesian
applications). The algorithm can be seen as a computational generalization
of the Laplace approximation suitable for skew or multimodal densities.

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
