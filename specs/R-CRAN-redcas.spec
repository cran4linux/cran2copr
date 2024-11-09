%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  redcas
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          An Interface to the Computer Algebra System 'REDUCE'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods 
Requires:         R-methods 

%description
'REDUCE' is a portable general-purpose computer algebra system supporting
scalar, vector, matrix and tensor algebra, symbolic differential and
integral calculus, arbitrary precision numerical calculations and output
in 'LaTeX' format. 'REDUCE' is based on 'Lisp' and is available on the two
dialects 'Portable Standard Lisp' ('PSL') and 'Codemist Standard Lisp'
('CSL'). The 'redcas' package provides an interface for executing
arbitrary 'REDUCE' code interactively from 'R', returning output as
character vectors. 'R' code and 'REDUCE' code can be interspersed. It also
provides a specialized function for calling the 'REDUCE' feature for
solving systems of equations, returning the output as an 'R' object
designed for the purpose. A further specialized function uses 'REDUCE'
features to generate 'LaTeX' output and post-processes this for direct use
in 'LaTeX' documents, e.g. using 'Sweave'.

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
