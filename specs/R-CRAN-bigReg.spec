%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bigReg
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Linear Models (GLM) for Large Data Sets

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-MASS >= 7.3.39
BuildRequires:    R-CRAN-Rcpp >= 1.0.11
BuildRequires:    R-CRAN-RcppArmadillo >= 0.5.200.1.0
BuildRequires:    R-CRAN-uuid >= 0.1.2
BuildRequires:    R-parallel 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-MASS >= 7.3.39
Requires:         R-CRAN-Rcpp >= 1.0.11
Requires:         R-CRAN-uuid >= 0.1.2
Requires:         R-parallel 
Requires:         R-methods 
Requires:         R-stats 

%description
Allows the user to carry out GLM on very large data sets. Data can be
created using the data_frame() function and appended to the object with
object$append(data); data_frame and data_matrix objects are available that
allow the user to store large data on disk. The data is stored as doubles
in binary format and any character columns are transformed to factors and
then stored as numeric (binary) data while a look-up table is stored in a
separate .meta_data file in the same folder. The data is stored in blocks
and GLM regression algorithm is modified and carries out a MapReduce- like
algorithm to fit the model. The functions bglm(), and summary() and
bglm_predict() are available for creating and post-processing of models.
The library requires Armadillo installed on your system. It may not
function on windows since multi-core processing is done using mclapply()
which forks R on Unix/Linux type operating systems.

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
