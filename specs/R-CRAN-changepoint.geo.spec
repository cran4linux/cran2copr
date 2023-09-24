%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  changepoint.geo
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Geometrically Inspired Multivariate Changepoint Detection

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-changepoint 
BuildRequires:    R-CRAN-changepoint.np 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-changepoint 
Requires:         R-CRAN-changepoint.np 
Requires:         R-methods 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Rdpack 

%description
Implements the high-dimensional changepoint detection method GeomCP and
the related mappings used for changepoint detection. These methods view
the changepoint problem from a geometrical viewpoint and aim to extract
relevant geometrical features in order to detect changepoints. The
geomcp() function should be your first point of call. References: Grundy
et al. (2020) <doi:10.1007/s11222-020-09940-y>.

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
