%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ctmva
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Continuous-Time Multivariate Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-polynom 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-polynom 

%description
Implements a basis function or functional data analysis framework for
several techniques of multivariate analysis in continuous-time setting.
Specifically, we introduced continuous-time analogues of several classical
techniques of multivariate analysis, such as principal component analysis,
canonical correlation analysis, Fisher linear discriminant analysis,
K-means clustering, and so on. Details are in Biplab Paul and Philip T
Reiss (2022) "Continuous-time multivariate analysis"; James O Ramsay,
Bernard W Silverman (2005) <ISBN:978-0-387-22751-1> "Functional Data
Analysis"; James O Ramsay, Giles Hooker and Spencer Graves (2009)
<ISBN:978-0-387-98185-7> "Functional Data Analysis with R and MATLAB".

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
