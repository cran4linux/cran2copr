%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CaseBasedReasoning
%global packver   0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Case Based Reasoning

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RcppParallel 
Requires:         R-CRAN-rms 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-ggplot2 

%description
Case-based reasoning is a problem-solving methodology that involves
solving a new problem by referring to the solution of a similar problem in
a large set of previously solved problems. The key aspect of Case Based
Reasoning is to determine the problem that "most closely" matches the new
problem at hand. This is achieved by defining a family of distance
functions and using these distance functions as parameters for local
averaging regression estimates of the final result. The optimal distance
function is chosen based on a specific error measure used in regression
estimation. This approach allows for efficient problem-solving by
leveraging past experiences and adapting solutions from similar cases. The
underlying concept is inspired by the work of Dippon J. et al. (2002)
<doi:10.1016/S0167-9473(02)00058-0>.

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
