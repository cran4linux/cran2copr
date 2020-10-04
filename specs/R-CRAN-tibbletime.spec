%global packname  tibbletime
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Time Aware Tibbles

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-zoo >= 1.8.0
BuildRequires:    R-CRAN-lubridate >= 1.6.0
BuildRequires:    R-CRAN-glue >= 1.1.1
BuildRequires:    R-CRAN-dplyr >= 0.7.4
BuildRequires:    R-CRAN-hms >= 0.4
BuildRequires:    R-CRAN-tidyselect >= 0.2.5
BuildRequires:    R-CRAN-purrr >= 0.2.3
BuildRequires:    R-CRAN-assertthat >= 0.2.0
BuildRequires:    R-CRAN-vctrs >= 0.2.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.7
BuildRequires:    R-CRAN-rlang >= 0.1.6
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-zoo >= 1.8.0
Requires:         R-CRAN-lubridate >= 1.6.0
Requires:         R-CRAN-glue >= 1.1.1
Requires:         R-CRAN-dplyr >= 0.7.4
Requires:         R-CRAN-hms >= 0.4
Requires:         R-CRAN-tidyselect >= 0.2.5
Requires:         R-CRAN-purrr >= 0.2.3
Requires:         R-CRAN-assertthat >= 0.2.0
Requires:         R-CRAN-vctrs >= 0.2.0
Requires:         R-CRAN-Rcpp >= 0.12.7
Requires:         R-CRAN-rlang >= 0.1.6
Requires:         R-CRAN-lifecycle 

%description
Built on top of the 'tibble' package, 'tibbletime' is an extension that
allows for the creation of time aware tibbles. Some immediate advantages
of this include: the ability to perform time-based subsetting on tibbles,
quickly summarising and aggregating results by time periods, and creating
columns that can be used as 'dplyr' time-based groups.

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
