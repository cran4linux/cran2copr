%global __brp_check_rpaths %{nil}
%global packname  trustOptim
%global packver   0.8.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.7.1
Release:          1%{?dist}%{?buildtag}
Summary:          Trust Region Optimization for Nonlinear Functions with Sparse Hessians

License:          MPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildRequires:    R-CRAN-Matrix >= 1.2.18
BuildRequires:    R-CRAN-Rcpp >= 1.0.3
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.7.0
BuildRequires:    R-methods 
Requires:         R-CRAN-Matrix >= 1.2.18
Requires:         R-CRAN-Rcpp >= 1.0.3
Requires:         R-methods 

%description
Trust region algorithm for nonlinear optimization. Efficient when the
Hessian of the objective function is sparse (i.e., relatively few nonzero
cross-partial derivatives). See Braun, M. (2014)
<doi:10.18637/jss.v060.i04>.

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
