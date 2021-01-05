%global packname  JuliaCall
%global packver   0.17.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.17.2
Release:          1%{?dist}%{?buildtag}
Summary:          Seamless Integration Between R and 'Julia'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         julia
BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-knitr >= 1.28
BuildRequires:    R-CRAN-Rcpp >= 0.12.7
BuildRequires:    R-utils 
Requires:         R-CRAN-knitr >= 1.28
Requires:         R-CRAN-Rcpp >= 0.12.7
Requires:         R-utils 

%description
Provides an R interface to 'Julia', which is a high-level,
high-performance dynamic programming language for numerical computing, see
<https://julialang.org/> for more information. It provides a high-level
interface as well as a low-level interface. Using the high level
interface, you could call any 'Julia' function just like any R function
with automatic type conversion. Using the low level interface, you could
deal with C-level SEXP directly while enjoying the convenience of using a
high-level programming language like 'Julia'.

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
