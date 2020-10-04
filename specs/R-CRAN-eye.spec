%global packname  eye
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}%{?buildtag}
Summary:          Analysis of Eye Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.0.1
BuildRequires:    R-CRAN-cli >= 2.0.2
BuildRequires:    R-CRAN-lubridate >= 1.7.8
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-english >= 1.2.5
BuildRequires:    R-CRAN-tidyselect >= 1.1.0
BuildRequires:    R-CRAN-tidyr >= 1.0.3
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 0.4.6
BuildRequires:    R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-tibble >= 3.0.1
Requires:         R-CRAN-cli >= 2.0.2
Requires:         R-CRAN-lubridate >= 1.7.8
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-english >= 1.2.5
Requires:         R-CRAN-tidyselect >= 1.1.0
Requires:         R-CRAN-tidyr >= 1.0.3
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-rlang >= 0.4.6
Requires:         R-CRAN-purrr >= 0.3.4

%description
A tool to facilitate common tasks in ophthalmic research: Conversion
between different visual acuity notations (Snellen, logMAR and ETDRS),
counting of patients, recode right and left eyes and reshape eye side
specific variables between wide and long format. The 'eye' package also
contains a real life data set of people with intravitreal injections with
anti-vascular endothelial growth factor (anti-VEGF), made available by
Fasler et al. (2019) <doi:10.1136/bmjopen-2018-027441>. Visual acuity
conversion is based on Schulze-Bonsel et al. (2006)
<doi:10.1167/iovs.05-0981>, Gregori et al. (2010)
<doi:10.1097/iae.0b013e3181d87e04>, Beck et al. (2003)
<doi:10.1016/s0002-9394(02)01825-1> and Bach (2007)
<http:michaelbach.de/sci/acuity.html>.

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
