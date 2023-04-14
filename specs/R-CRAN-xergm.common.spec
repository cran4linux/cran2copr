%global __brp_check_rpaths %{nil}
%global packname  xergm.common
%global packver   1.7.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.8
Release:          3%{?dist}%{?buildtag}
Summary:          Common Infrastructure for Extensions of Exponential Random GraphModels

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ergm >= 3.5.1
BuildRequires:    R-CRAN-network >= 1.13.0
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-CRAN-ergm >= 3.5.1
Requires:         R-CRAN-network >= 1.13.0
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-stats 

%description
Datasets and definitions of generic functions used in dependencies of the
'xergm' package.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
