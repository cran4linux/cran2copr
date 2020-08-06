%global packname  migest
%global packver   1.8.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.2
Release:          1%{?dist}
Summary:          Methods for the Indirect Estimation of Bilateral Migration

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-magrittr 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-utils 

%description
Indirect methods for estimating bilateral migration flows in the presence
of partial or missing data, including the estimation of bilateral
migration flows from changes in bilateral migrant stock tables (e.g. Abel
(2013) <doi:10.4054/DemRes.2013.28.18>).

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
