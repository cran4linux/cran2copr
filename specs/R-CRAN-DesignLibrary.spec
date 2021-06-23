%global __brp_check_rpaths %{nil}
%global packname  DesignLibrary
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Library of Research Designs

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fabricatr >= 0.8.0
BuildRequires:    R-CRAN-DeclareDesign >= 0.17.0
BuildRequires:    R-CRAN-randomizr >= 0.16.1
BuildRequires:    R-CRAN-estimatr >= 0.16.0
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-glue 
Requires:         R-CRAN-fabricatr >= 0.8.0
Requires:         R-CRAN-DeclareDesign >= 0.17.0
Requires:         R-CRAN-randomizr >= 0.16.1
Requires:         R-CRAN-estimatr >= 0.16.0
Requires:         R-CRAN-generics 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-glue 

%description
A simple interface to build designs using the package 'DeclareDesign'. In
one line of code, users can specify the parameters of individual designs
and diagnose their properties. The designers can also be used to compare
performance of a given design across a range of combinations of
parameters, such as effect size, sample size, and assignment
probabilities.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
