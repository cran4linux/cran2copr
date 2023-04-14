%global __brp_check_rpaths %{nil}
%global packname  aoos
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          3%{?dist}%{?buildtag}
Summary:          Another Object Orientation System

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-roxygen2 
Requires:         R-methods 
Requires:         R-CRAN-magrittr 
Requires:         R-utils 
Requires:         R-CRAN-roxygen2 

%description
Another implementation of object-orientation in R. It provides syntactic
sugar for the S4 class system and two alternative new implementations. One
is an experimental version built around S4 and the other one makes it more
convenient to work with lists as objects.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
