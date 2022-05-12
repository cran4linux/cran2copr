%global __brp_check_rpaths %{nil}
%global packname  ecolMod
%global packver   1.2.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.6.2
Release:          1%{?dist}%{?buildtag}
Summary:          "A Practical Guide to Ecological Modelling - Using R as a Simulation Platform"

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.01
Requires:         R-core >= 2.01
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-CRAN-shape 
BuildRequires:    R-CRAN-diagram 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-rootSolve 
Requires:         R-CRAN-shape 
Requires:         R-CRAN-diagram 
Requires:         R-CRAN-deSolve 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Figures, data sets and examples from the book "A practical guide to
ecological modelling - using R as a simulation platform" by Karline
Soetaert and Peter MJ Herman (2009). Springer. All figures from chapter x
can be generated by "demo(chapx)", where x = 1 to 11. The R-scripts of the
model examples discussed in the book are in subdirectory "examples",
ordered per chapter. Solutions to model projects are in the same
subdirectories.

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
