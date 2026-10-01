%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  latexr
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Translate 'LaTeX' Formulas to R Code

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.4.0
BuildRequires:    R-CRAN-purrr >= 0.3.0
Requires:         R-CRAN-R6 >= 2.4.0
Requires:         R-CRAN-purrr >= 0.3.0

%description
Implements a minimal 'LaTeX' parser that translates mathematical formulas
into R code strings. Supports arithmetic operators, implicit
multiplication, fractions, Greek letters, common mathematical functions,
and statistical notation for means, medians, and rolling sums. Input from
visual formula editors such as 'MathQuill' is normalized automatically,
and the resulting string can be evaluated with parse() and eval(), or
converted into an R function with latex2fun(). The implementation follows
the tree-walking interpreter design of Nystrom (2021)
<https://craftinginterpreters.com/>.

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
