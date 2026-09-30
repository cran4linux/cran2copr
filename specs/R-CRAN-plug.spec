%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  plug
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Secure and Intuitive Access to 'Plug' Interface

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr2 >= 1.0.0
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-keyring 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-httr2 >= 1.0.0
Requires:         R-CRAN-glue 
Requires:         R-CRAN-keyring 
Requires:         R-CRAN-tibble 

%description
Provides a secure and user-friendly interface to interact with the 'Plug'
<https://plugbytpf.com.br> 'API'. It enables developers to store and
manage credentials and tokens securely using the 'keyring' package, and to
retrieve data from 'API' endpoints with the 'httr2' package, using 'SQL'
queries built safely from templates. Designed for simplicity and security,
the package facilitates seamless integration with the 'Plug' ecosystem.

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
