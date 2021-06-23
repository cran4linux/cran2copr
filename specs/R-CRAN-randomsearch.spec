%global __brp_check_rpaths %{nil}
%global packname  randomsearch
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Random Search for Expensive Functions

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate >= 1.8.2
BuildRequires:    R-CRAN-smoof >= 1.5.1
BuildRequires:    R-CRAN-parallelMap >= 1.3
BuildRequires:    R-CRAN-ParamHelpers >= 1.10
BuildRequires:    R-CRAN-fs 
Requires:         R-CRAN-checkmate >= 1.8.2
Requires:         R-CRAN-smoof >= 1.5.1
Requires:         R-CRAN-parallelMap >= 1.3
Requires:         R-CRAN-ParamHelpers >= 1.10
Requires:         R-CRAN-fs 

%description
Simple Random Search function for the 'smoof' and 'ParamHelpers' ecosystem
with termination criteria and parallelization.

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
