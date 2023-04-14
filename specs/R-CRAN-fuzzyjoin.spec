%global __brp_check_rpaths %{nil}
%global packname  fuzzyjoin
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          3%{?dist}%{?buildtag}
Summary:          Join Tables Together on Inexact Matching

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 0.8.1
BuildRequires:    R-CRAN-tidyr >= 0.4.0
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-dplyr >= 0.8.1
Requires:         R-CRAN-tidyr >= 0.4.0
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-tibble 

%description
Join tables together based not on whether columns match exactly, but
whether they are similar by some comparison. Implementations include
string distance and regular expression matching.

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
