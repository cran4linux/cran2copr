%global packname  Spillover
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Spillover Index Based on VAR Modelling

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-vars 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-fastSOM 
Requires:         R-CRAN-vars 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-fastSOM 

%description
A user-friendly tool for estimating both total and directional volatility
spillovers based on Diebold and Yilmaz (2009, 2012). It also provides the
user with rolling estimation for total and net indices. User can find both
orthogonalized and generalized versions for each kind of measures. See
Diebold and Yilmaz (2009, 2012) find them at
<doi:10.1111/j.1468-0297.2008.02208.x> and
<doi:10.1016/j.ijforecast.2011.02.006>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
