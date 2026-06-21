%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  neuralnetwork
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Compact Multilayer Perceptrons

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-Rcpp 

%description
A small multilayer perceptron implementation for 'R'. It supports
regression and classification, multiple hidden layers, mini-batch
training, Adam, SGD, momentum, Nesterov, RPROP, GRPROP and L-BFGS
optimizers, dropout, L2 regularization, early stopping, convergence
thresholds, gradient clipping, sample and class weights, callback hooks,
target scaling and robust Huber loss for regression, 'Rcpp' forward-pass
kernels, formula interfaces, model evaluation with balanced classification
metrics, cross-validation, compact tuning, permutation importance, model
persistence helpers, and 'S3' prediction methods. Methods follow
Rumelhart, Hinton and Williams (1986) <doi:10.1038/323533a0>, with
optimizers including Riedmiller and Braun (1993)
<doi:10.1109/ICNN.1993.298623>, Nocedal (1980)
<doi:10.1090/S0025-5718-1980-0572855-7>, and Kingma and Ba (2014)
<doi:10.48550/arXiv.1412.6980>.

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
