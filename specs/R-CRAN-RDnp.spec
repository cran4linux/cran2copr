%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RDnp
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Test for Complete Independence in High-Dimensions

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cellWise 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-cellWise 
Requires:         R-CRAN-MASS 

%description
Test Statistics for Independence in High-Dimensional Datasets. This
package consists of two functions to perform the complete independence
test based on test statistics proposed by Bulut (unpublished yet) and
suggested by Najarzadeh (2021) <doi: 10.1080/03610926.2019.1702699>. The
Bulut's statistic is not sensitive to outliers in high-dimensional data,
unlike one of Najarzadeh (2021) <doi: 10.1080/03610926.2019.1702699>. So,
the Bulut's statistic can be performed robustly by using RDnp function.

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
