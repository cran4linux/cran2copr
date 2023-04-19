%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nndiagram
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Generator of 'LaTeX' Code for Drawing Neural Network Diagrams with 'TikZ'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-utils 

%description
Generates 'LaTeX' code for drawing well-formatted neural network diagrams
with 'TikZ'. Users have to define number of neurons on each layer, and
optionally define neuron connections they would like to keep or omit,
layers they consider to be oversized and neurons they would like to draw
with lighter color. They can also specify the title of diagram, color,
opacity of figure, labels of layers, input and output neurons. In
addition, this package helps to produce 'LaTeX' code for drawing
activation functions which are crucial in neural network analysis. To make
the code work in a 'LaTeX' editor, users need to install and import some
'TeX' packages including 'TikZ' in the setting of 'TeX' file.

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
