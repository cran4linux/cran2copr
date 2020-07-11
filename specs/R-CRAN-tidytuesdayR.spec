%global packname  tidytuesdayR
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Access the Weekly 'TidyTuesday' Project Dataset

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-tools >= 3.1.0
BuildRequires:    R-CRAN-lubridate >= 1.7.0
BuildRequires:    R-CRAN-xml2 >= 1.2.0
BuildRequires:    R-CRAN-readxl >= 1.0.0
BuildRequires:    R-CRAN-readr >= 1.0.0
BuildRequires:    R-CRAN-rvest >= 0.3.2
BuildRequires:    R-CRAN-purrr >= 0.2.5
BuildRequires:    R-CRAN-rstudioapi >= 0.2
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-usethis 
Requires:         R-tools >= 3.1.0
Requires:         R-CRAN-lubridate >= 1.7.0
Requires:         R-CRAN-xml2 >= 1.2.0
Requires:         R-CRAN-readxl >= 1.0.0
Requires:         R-CRAN-readr >= 1.0.0
Requires:         R-CRAN-rvest >= 0.3.2
Requires:         R-CRAN-purrr >= 0.2.5
Requires:         R-CRAN-rstudioapi >= 0.2
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-usethis 

%description
'TidyTuesday' is a project by the 'R4DS Online Learning Community' in
which they post a weekly dataset onto post a weekly dataset in a public
data repository (<https://github.com/rfordatascience/tidytuesday>) for
people to analyze and visualize. This package provides the tools to easily
download this data and the description of the source.

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
