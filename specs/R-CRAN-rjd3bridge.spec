%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rjd3bridge
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bridge Between 'RJDemetra' (V2) and 'rjd3' (V3)

License:          EUPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rjd3toolkit >= 3.3.0
BuildRequires:    R-CRAN-rjd3x13 >= 3.3.0
BuildRequires:    R-CRAN-rjd3tramoseats >= 3.3.0
BuildRequires:    R-CRAN-RJDemetra >= 0.2.7
BuildRequires:    R-CRAN-rjd3jars >= 0.0.5
BuildRequires:    R-CRAN-rJava 
Requires:         R-CRAN-rjd3toolkit >= 3.3.0
Requires:         R-CRAN-rjd3x13 >= 3.3.0
Requires:         R-CRAN-rjd3tramoseats >= 3.3.0
Requires:         R-CRAN-RJDemetra >= 0.2.7
Requires:         R-CRAN-rjd3jars >= 0.0.5
Requires:         R-CRAN-rJava 

%description
Provides bidirectional tools to convert seasonal adjustment models and
specifications between 'RJDemetra' ('JDemetra+' v2) and the 'rjd3'
ecosystem ('JDemetra+' v3, packages 'rjd3x13' and 'rjd3tramoseats').
Facilitates workflow migration and backward compatibility analysis.

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
