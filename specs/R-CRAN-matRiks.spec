%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  matRiks
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Generates Raven-Like Matrices According to Rules

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-DescTools 
Requires:         R-CRAN-DescTools 

%description
Generates Raven like matrices according to different rules and the
response list associated to the matrix. The package can generate matrices
composed of 4 or 9 cells, along with a response list of 11 elements (the
correct response + 10 incorrect responses). The matrices can be generated
according to both logical rules (i.e., the relationships between the
elements in the matrix are manipulated to create the matrix) and
visual-spatial rules (i.e., the visual or spatial characteristics of the
elements are manipulated to generate the matrix). The graphical elements
of this package are based on the 'DescTools' package. This package has
been developed within the PRIN2020 Project (Prot. 20209WKCLL) titled
"Computerized, Adaptive and Personalized Assessment of Executive Functions
and Fluid Intelligence" and founded by the Italian Ministry of Education
and Research.

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
