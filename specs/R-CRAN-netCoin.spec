%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  netCoin
%global packver   2.1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.9
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive Analytic Networks

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3
BuildRequires:    R-CRAN-GPArotation >= 2022.4
BuildRequires:    R-CRAN-Matrix >= 1.2.4
BuildRequires:    R-CRAN-rD3plot >= 1.1.37
BuildRequires:    R-CRAN-haven >= 1.1.0
BuildRequires:    R-CRAN-igraph >= 1.0.1
BuildRequires:    R-methods 
Requires:         R-CRAN-MASS >= 7.3
Requires:         R-CRAN-GPArotation >= 2022.4
Requires:         R-CRAN-Matrix >= 1.2.4
Requires:         R-CRAN-rD3plot >= 1.1.37
Requires:         R-CRAN-haven >= 1.1.0
Requires:         R-CRAN-igraph >= 1.0.1
Requires:         R-methods 

%description
Create interactive analytic networks. It joins the data analysis power of
R to obtain coincidences, co-occurrences and correlations, and the
visualization libraries of 'JavaScript' in one package.

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
