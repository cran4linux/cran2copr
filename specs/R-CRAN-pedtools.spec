%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pedtools
%global packver   2.8.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.8.2
Release:          1%{?dist}%{?buildtag}
Summary:          Creating and Working with Pedigrees and Marker Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-kinship2 
BuildRequires:    R-CRAN-pedmut 
Requires:         R-CRAN-kinship2 
Requires:         R-CRAN-pedmut 

%description
A comprehensive collection of tools for creating, manipulating and
visualising pedigrees and genetic marker data. Pedigrees can be read from
text files or created on the fly with built-in functions. A range of
utilities enable modifications like adding or removing individuals,
breaking loops, and merging pedigrees. An online tool for creating
pedigrees interactively, based on 'pedtools', is available at
<https://magnusdv.shinyapps.io/quickped>. 'pedtools' is the hub of the
'pedsuite', a collection of packages for pedigree analysis. A detailed
presentation of the 'pedsuite' is given in the book 'Pedigree Analysis in
R' (Vigeland, 2021, ISBN:9780128244302).

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
