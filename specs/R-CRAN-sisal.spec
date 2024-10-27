%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sisal
%global packver   0.49
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.49
Release:          1%{?dist}%{?buildtag}
Summary:          Sequential Input Selection Algorithm

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-R.matlab 
BuildRequires:    R-CRAN-R.methodsS3 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-R.matlab 
Requires:         R-CRAN-R.methodsS3 

%description
Implements the SISAL algorithm by Tikka and Hollmén. It is a sequential
backward selection algorithm which uses a linear model in a
cross-validation setting. Starting from the full model, one variable at a
time is removed based on the regression coefficients. From this set of
models, a parsimonious (sparse) model is found by choosing the model with
the smallest number of variables among those models where the validation
error is smaller than a threshold. Also implements extensions which
explore larger parts of the search space and/or use ridge regression
instead of ordinary least squares.

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
