%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  REPPlab
%global packver   0.9.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.6
Release:          1%{?dist}%{?buildtag}
Summary:          R Interface to 'EPP-Lab', a Java Program for Exploratory Projection Pursuit

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildArch:        noarch
BuildRequires:    R-CRAN-LDRTools >= 0.2
BuildRequires:    R-CRAN-rJava 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
Requires:         R-CRAN-LDRTools >= 0.2
Requires:         R-CRAN-rJava 
Requires:         R-CRAN-lattice 
Requires:         R-utils 
Requires:         R-graphics 

%description
An R Interface to 'EPP-lab' v1.0. 'EPP-lab' is a Java program for
projection pursuit using genetic algorithms written by Alain Berro and S.
Larabi Marie-Sainte and is included in the package.

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
