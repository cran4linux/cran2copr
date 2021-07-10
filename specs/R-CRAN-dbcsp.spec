%global __brp_check_rpaths %{nil}
%global packname  dbcsp
%global packver   0.0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Distance-Based Common Spatial Patterns

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-TSdist >= 3.7
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-parallelDist 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-geigen 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
Requires:         R-CRAN-TSdist >= 3.7
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-parallelDist 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-geigen 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 

%description
A way to apply Distance-Based Common Spatial Patterns (DB-CSP) techniques
in different fields, both classical Common Spatial Patterns (CSP) as well
as DB-CSP. The method is composed of two phases: applying the DB-CSP
algorithm and performing a classification. The main idea behind the CSP is
to use a linear transform to project data into low-dimensional subspace
with a projection matrix, in such a way that each row consists of weights
for signals. This transformation maximizes the variance of two-class
signal matrices.The dbcsp object is created to compute the projection
vectors. For exploratory and descriptive purpose, plot and boxplot
functions can be used. Functions train, predict and selectQ are
implemented for the classification step.

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
