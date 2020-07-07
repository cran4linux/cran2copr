%global packname  dmtools
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          3%{?dist}
Summary:          Tools for Validation the Dataset

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-lubridate >= 1.7.4
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-readxl >= 1.3.1
BuildRequires:    R-CRAN-dplyr >= 0.8.3
BuildRequires:    R-CRAN-purrr >= 0.3.3
Requires:         R-CRAN-lubridate >= 1.7.4
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-readxl >= 1.3.1
Requires:         R-CRAN-dplyr >= 0.8.3
Requires:         R-CRAN-purrr >= 0.3.3

%description
For checking the dataset from EDC(Electronic Data Capture) in clinical
trials. 'dmtools' can check laboratory, dates, WBCs(White Blood Cells)
count and rename the dataset. Laboratory - does the investigator correctly
estimate the laboratory analyzes? Dates - do all dates correspond to the
protocol's timeline? WBCs count - do absolute equal (all * relative) /
100? If the clinical trial has different lab reference ranges, 'dmtools'
also can help.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/ae.xlsx
%doc %{rlibdir}/%{packname}/dates.xlsx
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/drug.xlsx
%doc %{rlibdir}/%{packname}/forms
%doc %{rlibdir}/%{packname}/labs_refer_s01.xlsx
%doc %{rlibdir}/%{packname}/labs_refer_s02.xlsx
%doc %{rlibdir}/%{packname}/labs_refer.xlsx
%doc %{rlibdir}/%{packname}/preg.xlsx
%doc %{rlibdir}/%{packname}/vf.xlsx
%doc %{rlibdir}/%{packname}/wbcc.xlsx
%{rlibdir}/%{packname}/INDEX
