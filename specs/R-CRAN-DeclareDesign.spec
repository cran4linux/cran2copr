%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DeclareDesign
%global packver   1.0.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.10
Release:          1%{?dist}%{?buildtag}
Summary:          Declare and Diagnose Research Designs

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-randomizr >= 0.20.0
BuildRequires:    R-CRAN-estimatr >= 0.20.0
BuildRequires:    R-CRAN-fabricatr >= 0.10.0
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-methods 
Requires:         R-CRAN-randomizr >= 0.20.0
Requires:         R-CRAN-estimatr >= 0.20.0
Requires:         R-CRAN-fabricatr >= 0.10.0
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-generics 
Requires:         R-methods 

%description
Researchers can characterize and learn about the properties of research
designs before implementation using `DeclareDesign`. Ex ante declaration
and diagnosis of designs can help researchers clarify the strengths and
limitations of their designs and to improve their properties, and can help
readers evaluate a research strategy prior to implementation and without
access to results. It can also make it easier for designs to be shared,
replicated, and critiqued.

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
