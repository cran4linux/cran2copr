%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  selection.index
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Selection Index in Plant Breeding

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-utils 
Requires:         R-utils 

%description
The aim of most plant breeding programmes is simultaneous improvement of
several characters. An objective method involving simultaneous selection
for several attributes then becomes necessary. It has been recognised that
most rapid improvements in the economic value is expected from selection
applied simultaneously to all the characters which determine the economic
value of a plant, and appropriate assigned weights to each character
according to their economic importance, heritability and correlations
between characters. So the selection for economic value is a complex
matter. If the component characters are combined together into an index in
such a way that when selection is applied to the index, as if index is the
character to be improved, most rapid improvement of economic value is
expected. Such an index was first proposed by Smith (1937
<doi:10.1111/j.1469-1809.1936.tb02143.x>) based on the Fisher's (1936
<doi:10.1111/j.1469-1809.1936.tb02137.x>) "discriminant function"
Dabholkar (1999
<https://books.google.co.in/books?id=mlFtumAXQ0oC&lpg=PA4&ots=Xgxp1qLuxS&dq=elements%%20of%%20biometrical%%20genetics&lr&pg=PP1#v=onepage&q&f=false>).
In this package selection index is calculated based on the Smith (1937)
selection index method.

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
