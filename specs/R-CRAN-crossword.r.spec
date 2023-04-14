%global __brp_check_rpaths %{nil}
%global packname  crossword.r
%global packver   0.3.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.6
Release:          3%{?dist}%{?buildtag}
Summary:          Generating Crosswords from Word Lists

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.2.0
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-jsonlite >= 1.5
BuildRequires:    R-CRAN-stringr >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 0.5.0
BuildRequires:    R-CRAN-r6extended >= 0.1.1
Requires:         R-CRAN-R6 >= 2.2.0
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-jsonlite >= 1.5
Requires:         R-CRAN-stringr >= 1.2.0
Requires:         R-CRAN-dplyr >= 0.5.0
Requires:         R-CRAN-r6extended >= 0.1.1

%description
Generate crosswords from a list of words.

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
