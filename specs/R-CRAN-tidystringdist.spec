%global __brp_check_rpaths %{nil}
%global packname  tidystringdist
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          3%{?dist}%{?buildtag}
Summary:          String Distance Calculation with Tidy Data Principles

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-attempt 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-attempt 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-tibble 

%description
Calculation of string distance following the tidy data principles. Built
on top of the 'stringdist' package.

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
