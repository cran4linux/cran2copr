%global __brp_check_rpaths %{nil}
%global packname  galigor
%global packver   0.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.5
Release:          1%{?dist}%{?buildtag}
Summary:          Collection of Packages for Internet Marketing

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.0.0
BuildRequires:    R-CRAN-tibble >= 1.4.2
BuildRequires:    R-CRAN-crayon >= 1.3.4
BuildRequires:    R-CRAN-gargle >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-rstudioapi >= 0.7
BuildRequires:    R-CRAN-purrr >= 0.2.4
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-ryandexdirect 
BuildRequires:    R-CRAN-rfacebookstat 
BuildRequires:    R-CRAN-rvkstat 
BuildRequires:    R-CRAN-rmytarget 
BuildRequires:    R-CRAN-rym 
BuildRequires:    R-CRAN-getProxy 
BuildRequires:    R-CRAN-rgoogleads 
BuildRequires:    R-CRAN-rappsflyer 
Requires:         R-CRAN-cli >= 3.0.0
Requires:         R-CRAN-tibble >= 1.4.2
Requires:         R-CRAN-crayon >= 1.3.4
Requires:         R-CRAN-gargle >= 1.2.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-rstudioapi >= 0.7
Requires:         R-CRAN-purrr >= 0.2.4
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-ryandexdirect 
Requires:         R-CRAN-rfacebookstat 
Requires:         R-CRAN-rvkstat 
Requires:         R-CRAN-rmytarget 
Requires:         R-CRAN-rym 
Requires:         R-CRAN-getProxy 
Requires:         R-CRAN-rgoogleads 
Requires:         R-CRAN-rappsflyer 

%description
Collection of packages for work with API 'Google Ads'
<https://developers.google.com/google-ads/api/docs/start>, 'Yandex Direct'
<https://yandex.ru/dev/direct/>, 'Yandex Metrica'
<https://yandex.ru/dev/metrika/>, 'MyTarget'
<https://target.my.com/help/advertisers/api_arrangement/ru>, 'Vkontakte'
<https://vk.com/dev/methods>, 'Facebook'
<https://developers.facebook.com/docs/marketing-apis/> and 'AppsFlyer'
<https://support.appsflyer.com/hc/en-us/articles/207034346-Using-Pull-API-aggregate-data>.
This packages allows you loading data from ads account and manage your ads
materials.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
