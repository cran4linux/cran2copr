%global packname  ecce
%global packver   1.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.7
Release:          2%{?dist}
Summary:          Translate English Words into Chinese, or Translate Chinese Wordsinto English

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-rjson 
Requires:         R-CRAN-stringr 

%description
If translate English words into Chinese, there is a faster way for R user.
'RYoudaoTranslate' package provides interface to 'Youdao'
<http://youdao.com/> translation open API for R user. 'entcn' package also
provides similar features. But it does not support Chinese words
translation into English, I have made some improvements on the basis of
this software. You can pass in a words or a vector consisting of multiple
words, ecce package support both English and Chinese translation. It also
support browse translation results in website.

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
