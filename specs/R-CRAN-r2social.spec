%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  r2social
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Seamless Integration of Sharing and Connect Buttons in Markdown and Apps

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel > 3.6
Requires:         R-core > 3.6
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-quickcode 
Requires:         R-utils 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-quickcode 

%description
Implementation of 'JQuery' <https://jquery.com> and 'CSS' styles to allow
easy incorporation of various social media elements on a page. The
elements include addition of share buttons or connect with us buttons or
hyperlink buttons to 'Shiny' applications or dashboards and 'Rmarkdown'
documents.Sharing capability on social media platforms including
'Facebook' <https://www.facebook.com>, 'Linkedin'
<https://www.linkedin.com>, 'X/Twitter' <https://x.com>, 'Tumblr'
<https://www.tumblr.com>, 'Pinterest' <https://www.pinterest.com>,
'Whatsapp' <https://www.whatsapp.com>, 'Reddit' <https://www.reddit.com>,
'Baidu' <https://www.baidu.com>, 'Blogger' <https://www.blogger.com>,
'Weibo' <https://www.weibo.com>, 'Instagram' <https://www.instagram.com>,
'Telegram' <https://www.telegram.me>, 'Youtube' <https://www.youtube.com>.

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
