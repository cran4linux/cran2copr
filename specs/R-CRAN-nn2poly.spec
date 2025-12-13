%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nn2poly
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Neural Network Weights Transformation into Polynomial Coefficients

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-pracma 

%description
Implements a method that builds the coefficients of a polynomial model
that performs almost equivalently as a given neural network (densely
connected). This is achieved using Taylor expansion at the activation
functions.  The obtained polynomial coefficients can be used to explain
features (and their interactions) importance in the neural network,
therefore working as a tool for interpretability or eXplainable Artificial
Intelligence (XAI). See Morala et al. 2021
<doi:10.1016/j.neunet.2021.04.036>, and 2023
<doi:10.1109/TNNLS.2023.3330328>.

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
