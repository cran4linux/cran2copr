%global packname  timetk
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          A Tool Kit for Working with Time Series

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-zoo >= 1.7.14
BuildRequires:    R-CRAN-lubridate >= 1.6.0
BuildRequires:    R-CRAN-tibble >= 1.2
BuildRequires:    R-CRAN-stringi >= 1.1.5
BuildRequires:    R-CRAN-readr >= 1.0.0
BuildRequires:    R-CRAN-xts >= 0.9.7
BuildRequires:    R-CRAN-dplyr >= 0.7.0
BuildRequires:    R-CRAN-tidyr >= 0.6.1
BuildRequires:    R-CRAN-padr >= 0.3.0
BuildRequires:    R-CRAN-purrr >= 0.2.2
BuildRequires:    R-CRAN-lazyeval >= 0.2.0
BuildRequires:    R-CRAN-recipes >= 0.1.4
BuildRequires:    R-CRAN-rlang >= 0.1.2
Requires:         R-CRAN-zoo >= 1.7.14
Requires:         R-CRAN-lubridate >= 1.6.0
Requires:         R-CRAN-tibble >= 1.2
Requires:         R-CRAN-stringi >= 1.1.5
Requires:         R-CRAN-readr >= 1.0.0
Requires:         R-CRAN-xts >= 0.9.7
Requires:         R-CRAN-dplyr >= 0.7.0
Requires:         R-CRAN-tidyr >= 0.6.1
Requires:         R-CRAN-padr >= 0.3.0
Requires:         R-CRAN-purrr >= 0.2.2
Requires:         R-CRAN-lazyeval >= 0.2.0
Requires:         R-CRAN-recipes >= 0.1.4
Requires:         R-CRAN-rlang >= 0.1.2

%description
Get the time series index (date or date-time component), time series
signature (feature extraction of date or date-time component for time
series machine learning), and time series summary (summary attributes
about time series). Create future time series based on properties of
existing time series index using logistic regression. Coerce between
time-based tibbles ('tbl') and 'xts', 'zoo', and 'ts'. Methods discussed
herein are commonplace in machine learning, and have been cited in various
literature. Refer to "Calendar Effects" in papers such as Taieb, Souhaib
Ben. "Machine learning strategies for multi-step-ahead time series
forecasting." Universit Libre de Bruxelles, Belgium (2014): 75-86.
<http://souhaib-bentaieb.com/pdf/2014_phd.pdf>.

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
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
