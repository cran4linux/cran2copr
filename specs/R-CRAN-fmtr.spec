%global __brp_check_rpaths %{nil}
%global packname  fmtr
%global packver   1.5.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.4
Release:          1%{?dist}%{?buildtag}
Summary:          Easily Apply Formats to Data

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-tibble 
Requires:         R-stats 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-Rcpp 

%description
Contains a set of functions that can be used to apply formats to data
frames or vectors.  The package aims to provide to functionality similar
to that of SAS® formats. Formats are assigned to the format attribute on
data frame columns.  Then when the fdata() function is called, a new data
frame is created with the column data formatted as specified.  The package
also contains a value() function to create a user-defined format, similar
to a SAS® user-defined format.

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
