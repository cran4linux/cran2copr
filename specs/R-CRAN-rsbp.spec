%global __brp_check_rpaths %{nil}
%global packname  rsbp
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Part Information from the Registry of Standard Biological Parts

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.0.3
BuildRequires:    R-CRAN-lubridate >= 1.7.9
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-reshape2 >= 1.4.4
BuildRequires:    R-CRAN-xml2 >= 1.3.2
BuildRequires:    R-CRAN-tidyr >= 1.1.1
BuildRequires:    R-CRAN-dplyr >= 0.4.0
BuildRequires:    R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-tibble >= 3.0.3
Requires:         R-CRAN-lubridate >= 1.7.9
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-reshape2 >= 1.4.4
Requires:         R-CRAN-xml2 >= 1.3.2
Requires:         R-CRAN-tidyr >= 1.1.1
Requires:         R-CRAN-dplyr >= 0.4.0
Requires:         R-CRAN-purrr >= 0.3.4

%description
Provides an R interface to the Registry of Standard Biological Parts API
maintained by the iGEM Foundation: <https://igem.org/Main_Page>.
Facilitates retrieval of the part number, authorship, date of entry, url,
short description, type, and sequence following the guidelines set forth
at <http://parts.igem.org/Registry_API/Guidelines>. All Registry content
falls under Creative Commons Attribution-ShareAlike:
<https://creativecommons.org/licenses/by-sa/4.0/>.

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
