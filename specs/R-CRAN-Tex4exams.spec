%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Tex4exams
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Generating 'Sweave' Code for 'R/exams' Questions in Mathematics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-numbers 
BuildRequires:    R-CRAN-fractional 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-polynom 
Requires:         R-CRAN-numbers 
Requires:         R-CRAN-fractional 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-polynom 

%description
When using the R package 'exams' to write mathematics questions in
'Sweave' files, the output of a lot of R functions need to be adjusted for
display in mathematical formulas. Specifically, the functions were
accumulated when writing questions for the topics of the mathematics
courses College Algebra, Precalculus, Calculus, Differential Equations,
Introduction to Probability, and Linear Algebra.  The output of the
developed functions can be used in 'Sweave' files.

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
