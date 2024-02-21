%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggVennDiagram
%global packver   1.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.2
Release:          1%{?dist}%{?buildtag}
Summary:          A 'ggplot2' Implement of Venn Diagram

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-venn >= 1.12
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-aplot 
BuildRequires:    R-CRAN-yulab.utils 
BuildRequires:    R-CRAN-forcats 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-venn >= 1.12
Requires:         R-CRAN-dplyr 
Requires:         R-methods 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-aplot 
Requires:         R-CRAN-yulab.utils 
Requires:         R-CRAN-forcats 

%description
Easy-to-use functions to generate 2-7 sets Venn or upset plot in
publication quality. 'ggVennDiagram' plot Venn or upset using well-defined
geometry dataset and 'ggplot2'. The shapes of 2-4 sets Venn use circles
and ellipses, while the shapes of 4-7 sets Venn use irregular polygons (4
has both forms), which are developed and imported from another package
'venn', authored by Adrian Dusa. We provided internal functions to
integrate shape data with user provided sets data, and calculated the
geometry of every regions/intersections of them, then separately plot Venn
in four components, set edges/labels, and region edges/labels. From
version 1.0, it is possible to customize these components as you demand in
ordinary 'ggplot2' grammar. From version 1.4.4, it supports unlimited
number of sets, as it can draw a plain upset plot automatically when
number of sets is more than 7.

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
