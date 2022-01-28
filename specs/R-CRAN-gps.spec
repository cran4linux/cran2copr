%global __brp_check_rpaths %{nil}
%global packname  gps
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          General P-Splines

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-stats 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-stats 
Requires:         R-splines 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Routines to construct general P-splines for non-uniform B-splines on
arbitrary knots, proposed by Li and Cao (2022) <arXiv:2201.06808>. This
P-spline variant extends the standard P-splines of Eilers and Marx (1996)
<doi:10.1214/ss/1038425655> that are tailored for uniform B-splines on
equidistant knots. Includes SparseD() for computing general difference
matrices, SparseS() for computing derivative penalty matrix or its sparse
root using a sandwich formula, etc. Also includes several demos on
B-splines and P-splines. Aims to facilitate other packages to implement
general P-splines as a smoothing tool in their model estimation framework.

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
