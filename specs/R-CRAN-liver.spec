%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  liver
%global packver   1.14
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.14
Release:          1%{?dist}%{?buildtag}
Summary:          "Eating the Liver of Data Science"

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-class 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-class 
Requires:         R-CRAN-ggplot2 

%description
Provides a collection of helper functions that make various techniques
from data science more user-friendly for non-experts. In this way, our aim
is to allow non-experts to become familiar with the techniques with only a
minimal level of coding knowledge. Indeed, following an ancient Persian
idiom, we refer to this as "eating the liver of data science" which could
be interpreted as "getting intimately close with data science". Examples
of procedures we include are: data partitioning for out-of-sample testing,
computing Mean Squared Error (MSE) for quantifying prediction accuracy,
and data transformation (z-score and min-max). Besides such helper
functions, the package also includes several interesting datasets that are
useful for multivariate analysis.

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
