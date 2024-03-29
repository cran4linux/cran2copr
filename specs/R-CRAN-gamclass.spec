%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gamclass
%global packver   0.62.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.62.5
Release:          1%{?dist}%{?buildtag}
Summary:          Functions and Data for a Course on Modern Regression and Classification

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-methods 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-latticeExtra 
Requires:         R-methods 

%description
Functions and data are provided that support a course that emphasizes
statistical issues of inference and generalizability. The functions are
designed to make it straightforward to illustrate the use of
cross-validation, the training/test approach, simulation, and model-based
estimates of accuracy.  Methods considered are Generalized Additive
Modeling, Linear and Quadratic Discriminant Analysis, Tree-based methods,
and Random Forests.

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
