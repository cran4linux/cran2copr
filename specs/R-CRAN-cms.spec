%global __brp_check_rpaths %{nil}
%global packname  cms
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate Medicare Reimbursement

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-utils >= 3.6
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-readr >= 1.3
BuildRequires:    R-CRAN-xml2 >= 1.3
BuildRequires:    R-CRAN-dplyr >= 0.8
BuildRequires:    R-CRAN-rlang >= 0.4
BuildRequires:    R-CRAN-rvest >= 0.3
BuildRequires:    R-CRAN-assertthat >= 0.2
Requires:         R-utils >= 3.6
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-readr >= 1.3
Requires:         R-CRAN-xml2 >= 1.3
Requires:         R-CRAN-dplyr >= 0.8
Requires:         R-CRAN-rlang >= 0.4
Requires:         R-CRAN-rvest >= 0.3
Requires:         R-CRAN-assertthat >= 0.2

%description
Uses the 'CMS' application programming interface
<https://dnav.cms.gov/api/healthdata> to provide users databases
containing yearly Medicare reimbursement rates in the United States. Data
can be acquired for the entire United States or only for specific
localities. Currently, support is only provided for the Medicare Physician
Fee Schedule, but support will be expanded for other 'CMS' databases in
future versions.

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
