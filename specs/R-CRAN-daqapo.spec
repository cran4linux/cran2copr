%global packname  daqapo
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Data Quality Assessment for Process-Oriented Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-xesreadR 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-bupaR 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-edeaR 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-miniUI 
BuildRequires:    R-CRAN-shiny 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-xesreadR 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-bupaR 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-edeaR 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-miniUI 
Requires:         R-CRAN-shiny 

%description
Provides a variety of methods to identify data quality issues in
process-oriented data, which are useful to verify data quality in a
process mining context. Builds on the class for activity logs implemented
in the package 'bupaR'. Methods to identify data quality issues either
consider each activity log entry independently (e.g. missing values,
activity duration outliers,...), or focus on the relation amongst several
activity log entries (e.g. batch registrations, violations of the expected
activity order,...).

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
