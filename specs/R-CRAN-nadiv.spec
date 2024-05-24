%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nadiv
%global packver   2.18.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.18.0
Release:          1%{?dist}%{?buildtag}
Summary:          (Non)Additive Genetic Relatedness Matrices

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-Matrix 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats 

%description
Constructs (non)additive genetic relationship matrices, and their
inverses, from a pedigree to be used in linear mixed effect models (A.K.A.
the 'animal model'). Also includes other functions to facilitate the use
of animal models. Some functions have been created to be used in
conjunction with the R package 'asreml' for the 'ASReml' software, which
can be obtained upon purchase from 'VSN' international
(<https://vsni.co.uk/software/asreml>).

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
