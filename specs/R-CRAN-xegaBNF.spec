%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  xegaBNF
%global packver   1.0.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Compile a Backus-Naur Form Specification into an R Grammar Object

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Translates a BNF (Backus-Naur Form) specification of a context-free
language into an R grammar object which consists of the start symbol, the
symbol table, the production table, and a short production table. The
short production table is non-recursive. The grammar object contains the
file name from which it was generated (without a path). In addition, it
provides functions to determine the type of a symbol (isTerminal() and
isNonterminal()) and functions to access the production table (rules() and
derives()). For the BNF specification, see Backus, John et al. (1962)
"Revised Report on the Algorithmic Language ALGOL 60". (ALGOL60 standards
page <http://www.algol60.org/2standards.htm>, html-edition
<https://www.masswerk.at/algol60/report.htm>) The grammar compiler is
based on the APL2 implementation in Geyer-Schulz, Andreas (1997,
ISBN:978-3-7908-0830-X).

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
