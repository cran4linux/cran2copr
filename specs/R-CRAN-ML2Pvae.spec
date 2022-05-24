%global __brp_check_rpaths %{nil}
%global packname  ML2Pvae
%global packver   1.0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Variational Autoencoder Models for IRT Parameter Estimation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-keras >= 2.3.0
BuildRequires:    R-CRAN-tensorflow >= 2.2.0
BuildRequires:    R-CRAN-reticulate >= 1.0
BuildRequires:    R-CRAN-tfprobability >= 0.11.0
Requires:         R-CRAN-keras >= 2.3.0
Requires:         R-CRAN-tensorflow >= 2.2.0
Requires:         R-CRAN-reticulate >= 1.0
Requires:         R-CRAN-tfprobability >= 0.11.0

%description
Based on the work of Curi, Converse, Hajewski, and Oliveira (2019)
<doi:10.1109/IJCNN.2019.8852333>. This package provides easy-to-use
functions which create a variational autoencoder (VAE) to be used for
parameter estimation in Item Response Theory (IRT) - namely the
Multidimensional Logistic 2-Parameter (ML2P) model. To use a neural
network as such, nontrivial modifications to the architecture must be
made, such as restricting the nonzero weights in the decoder according to
some binary matrix Q. The functions in this package allow for
straight-forward construction, training, and evaluation so that minimal
knowledge of 'tensorflow' or 'keras' is required.

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
