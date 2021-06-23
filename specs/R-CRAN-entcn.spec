%global __brp_check_rpaths %{nil}
%global packname  entcn
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Translate English Words into Chinese Words

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-bitops 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-RYoudaoTranslate 
Requires:         R-CRAN-bitops 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-rjson 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-RYoudaoTranslate 

%description
If translate English words into Chinese, you might consider looking up a
dictionary or online query, in fact, there is a faster way for R user.
Ke-Hao Wu (2014) <RYoudaoTranslate: R package provide functions to
translate English words into Chinese.> provides interface to Youdao
translation open API for R user. But this software is not very friendly to
use, I have made some improvements on the basis of this software. You can
pass in a words or a vector consisting of multiple words, which will
return the corresponding type of Chinese representation and be easy to
reuse.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
