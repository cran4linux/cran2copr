%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Rfuzzycoco
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Provides an R Interface to the 'FuzzyCoCo' C++ Library and Extends It

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-generics 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides and extends the 'Fuzzy Coco' algorithm by wrapping the
'FuzzyCoCo' 'C++' Library, cf
<https://github.com/Lonza-RND-Data-Science/fuzzycoco>. 'Fuzzy Coco'
constructs systems that predict the outcome of a human decision-making
process while providing an understandable explanation of a possible
reasoning leading to it.  The constructed fuzzy systems are composed of
rules and linguistic variables.  This package provides a 'S3' classic
interface (fit_xy()/fit()/predict()/evaluate()) and a
'tidymodels'/'parsnip' interface, a custom engine with custom iteration
stop criterion and progress bar support as well as a systematic
implementation that do not rely on genetic programming but rather explore
all possible combinations.

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
