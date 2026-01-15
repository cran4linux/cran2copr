%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  INLAtools
%global packver   0.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.7
Release:          1%{?dist}%{?buildtag}
Summary:          Functionalities for the 'INLA' Package

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3
Requires:         R-core >= 4.3
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-inlabru 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-inlabru 
Requires:         R-methods 
Requires:         R-utils 

%description
Contain code to work with a C struct, in short cgeneric, to define a
Gaussian Markov random (GMRF) model. The cgeneric contain code to specify
GMRF elements such as the graph and the precision matrix, and also the
initial and prior for its parameters, useful for model inference. It can
be accessed from a C program and is the recommended way to implement new
GMRF models in the 'INLA' package (<https://www.r-inla.org>). The
'INLAtools' implement functions to evaluate each one of the model
specifications from R. The implemented functionalities leverage the use of
'cgeneric' models and provide a way to debug the code as well to work with
the prior for the model parameters and to sample from it. A very useful
functionality is the Kronecker product method that creates a new model
from multiple cgeneric models. It also works with the rgeneric, the R
version of the cgeneric intended to easy try implementation of new GMRF
models. The Kronecker between two cgeneric models was used in Sterrantino
et. al. (2024) <doi:10.1007/s10260-025-00788-y>, and can be used to build
the spatio-temporal intrinsic interaction models for what the needed
constraints are automatically set.

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
