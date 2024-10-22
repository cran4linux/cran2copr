%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  VDPO
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Working with and Analyzing Functional Data of Varying Lengths

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-SOP 
BuildRequires:    R-splines 
BuildRequires:    R-stats 
Requires:         R-utils 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-SOP 
Requires:         R-splines 
Requires:         R-stats 

%description
Comprehensive set of tools for analyzing and manipulating functional data
with non-uniform lengths. This package addresses two common scenarios in
functional data analysis: Variable Domain Data, where the observation
domain differs across samples, and Partially Observed Data, where
observations are incomplete over the domain of interest. 'VDPO' enhances
the flexibility and applicability of functional data analysis in 'R'. See
Amaro et al. (2024) <doi:10.48550/arXiv.2401.05839>.

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
