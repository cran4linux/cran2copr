%global __brp_check_rpaths %{nil}
%global packname  usefun
%global packver   0.4.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.8
Release:          1%{?dist}%{?buildtag}
Summary:          A Collection of Useful Functions by John

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-dplyr 

%description
A set of general functions that I have used in various projects and in
other R packages. They support some miscellaneous operations on data
frames, matrices and vectors like adding a row on a ternary (3-value)
data.frame based on positive and negative vector-indicators, rearranging a
list of data.frames by rownames, pruning rows or columns of a data.frame
that contain only one specific value given by the user, pruning and
reordering a vector according to the common elements between its names and
elements of another given vector, finding the non-common elements between
two vectors (outer-section), normalization of a vector, matrix or
data.frame's numeric values in a specified range, pretty printing of
vector names and values in an R Markdown document. Also included is a
function that returns the statistics needed for plotting a ROC curve.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
