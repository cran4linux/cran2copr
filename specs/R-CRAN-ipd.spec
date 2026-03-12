%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ipd
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Inference on Predicted Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-gam 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-splines 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-tibble 
Requires:         R-methods 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-gam 
Requires:         R-CRAN-ranger 
Requires:         R-splines 
Requires:         R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-tibble 

%description
Performs valid statistical inference on predicted data (IPD) using recent
methods, where for a subset of the data, the outcomes have been predicted
by an algorithm. Provides a wrapper function with specified defaults for
the type of model and method to be used for estimation and inference.
Further provides methods for tidying and summarizing results. Salerno et
al., (2025) <doi:10.1093/bioinformatics/btaf055>.

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
