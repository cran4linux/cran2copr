%global __brp_check_rpaths %{nil}
%global packname  pipefittr
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Convert Nested Functions to Pipes

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rstudioapi >= 0.4
BuildRequires:    R-CRAN-shiny >= 0.13
BuildRequires:    R-CRAN-miniUI >= 0.1.1
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-rstudioapi >= 0.4
Requires:         R-CRAN-shiny >= 0.13
Requires:         R-CRAN-miniUI >= 0.1.1
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-stringr 

%description
To take nested function calls and convert them to a more readable form
using pipes from package 'magrittr'.

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
