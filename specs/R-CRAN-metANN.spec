%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  metANN
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Metaheuristic and Gradient-Based Optimization for Neural Network Training and Continuous Problems

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Provides tools for general-purpose continuous optimization and
feed-forward artificial neural network training using metaheuristic and
gradient-based optimization algorithms. The package supports benchmark
function optimization, regression, binary classification, and multi-class
classification with multilayer perceptrons. The package implements several
optimization methods, including particle swarm optimization Kennedy and
Eberhart (1995) <doi:10.1109/ICNN.1995.488968>, differential evolution
Storn and Price (1997) <doi:10.1023/A:1008202821328>, grey wolf optimizer
Mirjalili et al. (2014) <doi:10.1016/j.advengsoft.2013.12.007>, secretary
bird optimization Fu et al. (2024) <doi:10.1007/s10462-024-10729-y>, and
Adam Kingma and Ba (2015) <doi:10.48550/arXiv.1412.6980>.

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
