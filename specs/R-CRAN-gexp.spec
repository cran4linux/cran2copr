%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gexp
%global packver   1.0-21
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.21
Release:          1%{?dist}%{?buildtag}
Summary:          Generator of Experiments

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-CRAN-png 
Requires:         R-CRAN-mvtnorm 
Requires:         R-tcltk 
Requires:         R-CRAN-jpeg 
Requires:         R-CRAN-png 

%description
Generates experiments - simulating structured or experimental data as:
completely randomized design, randomized block design, latin square
design, factorial and split-plot experiments (Ferreira, 2008,
ISBN:8587692526; Naes et al., 2007 <doi:10.1002/qre.841>; Rencher et al.,
2007, ISBN:9780471754985; Montgomery, 2001, ISBN:0471316490).

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
