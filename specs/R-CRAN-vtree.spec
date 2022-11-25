%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  vtree
%global packver   5.6.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.6.4
Release:          1%{?dist}%{?buildtag}
Summary:          Display Information About Nested Subsets of a Data Frame

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-DiagrammeR 
BuildRequires:    R-CRAN-DiagrammeRsvg 
BuildRequires:    R-CRAN-rsvg 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-utf8 
Requires:         R-CRAN-DiagrammeR 
Requires:         R-CRAN-DiagrammeRsvg 
Requires:         R-CRAN-rsvg 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-utf8 

%description
A tool for calculating and drawing "variable trees". Variable trees
display information about nested subsets of a data frame.

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
