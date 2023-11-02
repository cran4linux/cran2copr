%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  liver
%global packver   1.15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.15
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
Offers a suite of helper functions to simplify various data science
techniques for non-experts. This package aims to enable individuals with
only a minimal level of coding knowledge to become acquainted with these
techniques in an accessible manner. Inspired by an ancient Persian idiom,
we liken this process to "eating the liver of data science," suggesting a
deep and intimate engagement with the field of data science. This package
includes functions for tasks such as data partitioning for out-of-sample
testing, calculating Mean Squared Error (MSE) to assess prediction
accuracy, and data transformations (z-score and min-max). In addition to
these helper functions, the 'liver' package also features several
intriguing datasets valuable for multivariate analysis.

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
