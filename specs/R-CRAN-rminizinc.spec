%global packname  rminizinc
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          R Interface to Use 'MiniZinc'

License:          Mozilla Public License Version 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rlist 
Requires:         R-CRAN-rjson 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rlist 

%description
Constraint optimization, or constraint programming, is the name given to
identifying feasible solutions out of a very large set of candidates,
where the problem can be modeled in terms of arbitrary constraints.
'MiniZinc' is a free and open-source constraint modeling language.
Constraint satisfaction and discrete optimization problems can be
formulated in a high-level modeling language. Models are compiled into an
intermediate representation that is understood by a wide range of solvers.
'MiniZinc' itself provides several solvers, for instance 'GeCode'. R users
can use the package to solve constraint programming problems without using
'MiniZinc' directly, modify existing 'MiniZinc' models and also create
their own models.

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
