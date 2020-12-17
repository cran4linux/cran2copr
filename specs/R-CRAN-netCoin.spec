%global packname  netCoin
%global packver   1.1.26
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.26
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive Analytic Networks

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix >= 1.2.4
BuildRequires:    R-CRAN-haven >= 1.1.0
BuildRequires:    R-CRAN-igraph >= 1.0.1
Requires:         R-CRAN-Matrix >= 1.2.4
Requires:         R-CRAN-haven >= 1.1.0
Requires:         R-CRAN-igraph >= 1.0.1

%description
Create interactive analytic networks. It joins the data analysis power of
R to obtain coincidences, co-occurrences and correlations, and the
visualization libraries of 'JavaScript' in one package. The methods are
described in Escobar and Martinez-Uribe (2020)
<doi:10.18637/jss.v093.i11>.

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
