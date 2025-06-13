%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  forestplot
%global packver   3.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Advanced Forest Plot Using 'grid' Graphics

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-abind 
Requires:         R-grid 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-abind 

%description
Allows the creation of forest plots with advanced features, such as
multiple confidence intervals per row, customizable fonts for individual
text elements, and flexible confidence interval drawing. It also supports
mixing text with mathematical expressions. The package extends the
application of forest plots beyond traditional meta-analyses, offering a
more general version of the original 'rmeta' package’s forestplot()
function. It relies heavily on the 'grid' package for rendering the plots.

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
