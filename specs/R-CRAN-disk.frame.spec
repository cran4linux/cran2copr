%global packname  disk.frame
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Larger-than-RAM Disk-Based Data Manipulation Framework

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-jsonlite >= 1.6
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-crayon >= 1.3.4
BuildRequires:    R-CRAN-glue >= 1.3.1
BuildRequires:    R-CRAN-fs >= 1.3.1
BuildRequires:    R-CRAN-future.apply >= 1.3.0
BuildRequires:    R-CRAN-future >= 1.14.0
BuildRequires:    R-CRAN-data.table >= 1.12.2
BuildRequires:    R-CRAN-dplyr >= 0.8.3
BuildRequires:    R-CRAN-fst >= 0.8.0
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-purrr >= 0.3.2
BuildRequires:    R-CRAN-assertthat >= 0.2.1
BuildRequires:    R-CRAN-globals >= 0.12.4
BuildRequires:    R-CRAN-Rcpp >= 0.12.13
BuildRequires:    R-CRAN-pryr >= 0.1.4
BuildRequires:    R-CRAN-furrr >= 0.1.0
Requires:         R-CRAN-jsonlite >= 1.6
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-crayon >= 1.3.4
Requires:         R-CRAN-glue >= 1.3.1
Requires:         R-CRAN-fs >= 1.3.1
Requires:         R-CRAN-future.apply >= 1.3.0
Requires:         R-CRAN-future >= 1.14.0
Requires:         R-CRAN-data.table >= 1.12.2
Requires:         R-CRAN-dplyr >= 0.8.3
Requires:         R-CRAN-fst >= 0.8.0
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-purrr >= 0.3.2
Requires:         R-CRAN-assertthat >= 0.2.1
Requires:         R-CRAN-globals >= 0.12.4
Requires:         R-CRAN-Rcpp >= 0.12.13
Requires:         R-CRAN-pryr >= 0.1.4
Requires:         R-CRAN-furrr >= 0.1.0

%description
A disk-based data manipulation tool for working with arbitrarily large
datasets as long as they fit on disk.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/figures
%doc %{rlibdir}/%{packname}/options.rmd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
