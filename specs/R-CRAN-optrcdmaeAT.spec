%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  optrcdmaeAT
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Optimal Row-Column Designs for Two-Colour cDNA Microarray Experiments

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    xorg-x11-server-Xvfb
BuildRequires:    R-devel >= 3.3.2
Requires:         R-core >= 3.3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-tcltk 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-igraph 
Requires:         R-tcltk 

%description
Computes A-, MV-, D- and E-optimal or near-optimal row-column designs for
two-colour cDNA microarray experiments using the linear fixed effects and
mixed effects models where the interest is in a comparison of all pairwise
treatment contrasts. The algorithms used in this package are based on the
array exchange and treatment exchange algorithms adopted from Debusho,
Gemechu and Haines (2018) <doi:10.1080/03610918.2018.1429617> algorithms
after adjusting for the row-column designs setup. The package also
provides an optional method of using the graphical user interface (GUI) R
package tcltk to ensure that it is user friendly.

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
xvfb-run %{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
