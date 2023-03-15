%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  laGP
%global packver   1.5-9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.9
Release:          1%{?dist}%{?buildtag}
Summary:          Local Approximate Gaussian Process Regression

License:          LGPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14
Requires:         R-core >= 2.14
BuildRequires:    R-CRAN-tgp 
BuildRequires:    R-parallel 
Requires:         R-CRAN-tgp 
Requires:         R-parallel 

%description
Performs approximate GP regression for large computer experiments and
spatial datasets.  The approximation is based on finding small local
designs for prediction (independently) at particular inputs. OpenMP and
SNOW parallelization are supported for prediction over a vast
out-of-sample testing set; GPU acceleration is also supported for an
important subroutine.  OpenMP and GPU features may require special
compilation.  An interface to lower-level (full) GP inference and
prediction is provided. Wrapper routines for blackbox optimization under
mixed equality and inequality constraints via an augmented Lagrangian
scheme, and for large scale computer model calibration, are also provided.
For details and tutorial, see Gramacy (2016 <doi:10.18637/jss.v072.i01>.

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
