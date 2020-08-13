%global packname  pointblank
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Validation of Local and Remote Data Tables

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-testthat >= 2.3.2
BuildRequires:    R-CRAN-yaml >= 2.2.1
BuildRequires:    R-CRAN-cli >= 2.0.2
BuildRequires:    R-CRAN-dbplyr >= 1.4.4
BuildRequires:    R-CRAN-fs >= 1.4.1
BuildRequires:    R-CRAN-glue >= 1.3.2
BuildRequires:    R-CRAN-knitr >= 1.28
BuildRequires:    R-CRAN-scales >= 1.1.1
BuildRequires:    R-CRAN-DBI >= 1.1.0
BuildRequires:    R-CRAN-tidyselect >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-digest >= 0.6.25
BuildRequires:    R-CRAN-rlang >= 0.4.6
BuildRequires:    R-CRAN-htmltools >= 0.4.0
BuildRequires:    R-CRAN-log4r >= 0.3.2
BuildRequires:    R-CRAN-blastula >= 0.3.1
BuildRequires:    R-CRAN-ggforce >= 0.3.1
BuildRequires:    R-CRAN-gt >= 0.2.1
BuildRequires:    R-CRAN-base64enc >= 0.1.3
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-testthat >= 2.3.2
Requires:         R-CRAN-yaml >= 2.2.1
Requires:         R-CRAN-cli >= 2.0.2
Requires:         R-CRAN-dbplyr >= 1.4.4
Requires:         R-CRAN-fs >= 1.4.1
Requires:         R-CRAN-glue >= 1.3.2
Requires:         R-CRAN-knitr >= 1.28
Requires:         R-CRAN-scales >= 1.1.1
Requires:         R-CRAN-DBI >= 1.1.0
Requires:         R-CRAN-tidyselect >= 1.1.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-digest >= 0.6.25
Requires:         R-CRAN-rlang >= 0.4.6
Requires:         R-CRAN-htmltools >= 0.4.0
Requires:         R-CRAN-log4r >= 0.3.2
Requires:         R-CRAN-blastula >= 0.3.1
Requires:         R-CRAN-ggforce >= 0.3.1
Requires:         R-CRAN-gt >= 0.2.1
Requires:         R-CRAN-base64enc >= 0.1.3
Requires:         R-CRAN-magrittr 

%description
Validate data in data frames, 'tibble' objects, and in database tables
(e.g., 'PostgreSQL' and 'MySQL'). Validation pipelines can be made using
easily-readable, consecutive validation steps. Upon execution of the
validation plan, several reporting options are available. User-defined
thresholds for failure rates allow for the determination of appropriate
reporting actions.

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
