%global __brp_check_rpaths %{nil}
%global packname  observer
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Observe and Check your Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.3
Requires:         R-core >= 3.1.3
BuildArch:        noarch
BuildRequires:    R-CRAN-bazar 
BuildRequires:    R-CRAN-bit 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
Requires:         R-CRAN-bazar 
Requires:         R-CRAN-bit 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-lazyeval 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tibble 
Requires:         R-utils 

%description
Checks that a given dataset passes user-specified rules. The main
functions are observe_if() and inspect().

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
