%global packname  googleTagManageR
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Access the 'Google Tag Manager' API using R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr >= 1.3.1
BuildRequires:    R-CRAN-googleAuthR >= 1.2.1
BuildRequires:    R-CRAN-future >= 1.2.0
BuildRequires:    R-CRAN-jsonlite >= 1.1
BuildRequires:    R-CRAN-dplyr >= 0.8.0
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-httr >= 1.3.1
Requires:         R-CRAN-googleAuthR >= 1.2.1
Requires:         R-CRAN-future >= 1.2.0
Requires:         R-CRAN-jsonlite >= 1.1
Requires:         R-CRAN-dplyr >= 0.8.0
Requires:         R-CRAN-assertthat 
Requires:         R-utils 
Requires:         R-CRAN-purrr 

%description
Interact with the 'Google Tag Manager' API
<https://developers.google.com/tag-manager/api/v2>, enabling scripted
deployments and updates across multiple tags, triggers, variables and
containers.

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
