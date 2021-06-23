%global __brp_check_rpaths %{nil}
%global packname  smoothedLasso
%global packver   1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6
Release:          1%{?dist}%{?buildtag}
Summary:          A Framework to Smooth L1 Penalized Regression Operators using Nesterov Smoothing

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-Matrix 

%description
We provide full functionality to smooth L1 penalized regression operators
and to compute regression estimates thereof. For this, the objective
function of a user-specified regression operator is first smoothed using
Nesterov smoothing (see Y. Nesterov (2005)
<doi:10.1007/s10107-004-0552-5>), resulting in a modified objective
function with explicit gradients everywhere. The smoothed objective
function and its gradient are minimized via BFGS, and the obtained
minimizer is returned. Using Nesterov smoothing, the smoothed objective
function can be made arbitrarily close to the original (unsmoothed) one.
In particular, the Nesterov approach has the advantage that it comes with
explicit accuracy bounds, both on the L1/L2 difference of the unsmoothed
to the smoothed objective functions as well as on their respective
minimizers (see G. Hahn, S.M. Lutz, N. Laha, C. Lange (2020)
<doi:10.1101/2020.09.17.301788>). A progressive smoothing approach is
provided which iteratively smoothes the objective function, resulting in
more stable regression estimates. A function to perform cross validation
for selection of the regularization parameter is provided.

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
