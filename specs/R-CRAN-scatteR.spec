%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  scatteR
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Generate Instance Space Based on Scagnostics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-scagnostics 
BuildRequires:    R-CRAN-GenSA 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rJava 
Requires:         R-CRAN-scagnostics 
Requires:         R-CRAN-GenSA 
Requires:         R-stats 
Requires:         R-CRAN-rJava 

%description
Generate bivariate data based on scatterplot features defined through
scagnostics. Scagnostics is an exploratory graphical tool that defines
nine features of a scatterplot based on the characteristics of three
geometric graphs defined on the scatterplot. The exact calculation of
these measurements are based on Wilkinson, L., Anand, A., & Grossman, R.
(2005) <doi:10.1109/INFVIS.2005.1532142>. Set the required values for the
scagnostic measurement type and the number of points that are needed to
generate a bivariate dataset that gives the expected scagnostic
measurements.

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
