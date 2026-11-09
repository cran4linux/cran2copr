%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  soilVAE
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Supervised Variational Autoencoder Regression via 'reticulate'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-reticulate >= 1.41
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-reticulate >= 1.41
Requires:         R-stats 
Requires:         R-utils 

%description
Supervised latent-variable regression for high-dimensional predictors such
as soil reflectance spectra. The model uses an encoder-decoder neural
network with a stochastic Gaussian latent representation regularized by a
Kullback-Leibler term, and a supervised prediction head trained jointly
with the reconstruction objective (Kingma and Welling (2014)
<doi:10.48550/arXiv.1312.6114>). Predictors and response are standardised
inside the model, so new data are scaled like the training data. The
implementation interfaces R with a 'Python' deep-learning backend ('Keras'
and 'TensorFlow') and provides utilities for installation, training with
early stopping, tuning, prediction, latent embeddings, and saving models.

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
