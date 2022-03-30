%global __brp_check_rpaths %{nil}
%global packname  RGAN
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Generative Adversarial Nets (GAN) in R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-torch 
BuildRequires:    R-CRAN-viridis 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-torch 
Requires:         R-CRAN-viridis 

%description
An easy way to get started with Generative Adversarial Nets (GAN) in R.
The GAN algorithm was initially described by Goodfellow et al. 2014
<https://proceedings.neurips.cc/paper/2014/file/5ca3e9b122f61f8f06494c97b1afccf3-Paper.pdf>.
A GAN can be used to learn the joint distribution of complex data by
comparison. A GAN consists of two neural networks a Generator and a
Discriminator, where the two neural networks play an adversarial minimax
game. Built-in GAN models make the training of GANs in R possible in one
line and make it easy to experiment with different design choices (e.g.
different network architectures, value functions, optimizers). The
built-in GAN models work with tabular data (e.g. to produce synthetic
data) and image data. Methods to post-process the output of GAN models to
enhance the quality of samples are available.

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
