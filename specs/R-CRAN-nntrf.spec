%global __brp_check_rpaths %{nil}
%global packname  nntrf
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Supervised Data Transformation by Means of Neural Network Hidden Layer

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.4
Requires:         R-core >= 3.2.4
BuildArch:        noarch
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-NeuralNetTools 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-NeuralNetTools 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-pracma 

%description
A supervised transformation of datasets is performed. The aim is similar
to that of Principal Component Analysis (PCA), that is, to carry out data
transformation and dimensionality reduction, but in a supervised way. This
is achieved by first training a 3-layer Multi-Layer Perceptron and then
using the activations of the hidden layer as a transformation of the input
features. In fact, it takes advantage of the change of representation
provided by the hidden layer of a neural network. This can be useful as
data pre-processing for Machine Learning methods in general, specially for
those that do not work well with many irrelevant or redundant features. It
uses the nnet package under the hood. Valls, J.M., Aler, R., Galvan, I.M.,
and Camacho, D. (2021). "Supervised data transformation and dimensionality
reduction with a 3-layer multi-layer perceptron for classification
problems". <doi:10.1007/s12652-020-02841-y> Rumelhart, D.E., Hinton, G.E.
and Williams, R.J. (1986) "Learning representations by back-propagating
errors" <doi:10.1038/323533a0>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
