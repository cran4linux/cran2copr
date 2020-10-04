%global packname  cwbtools
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tools to Create, Modify and Manage 'CWB' Corpora

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-RcppCWB >= 0.2.8
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-zen4R 
Requires:         R-CRAN-RcppCWB >= 0.2.8
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-pbapply 
Requires:         R-methods 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-zen4R 

%description
The 'Corpus Workbench' ('CWB', <http://cwb.sourceforge.net/>) offers a
classic and mature approach for working with large, linguistically and
structurally annotated corpora. The 'CWB' is memory efficient and its
design makes running queries fast (Evert and Hardie 2011,
<http://www.stefan-evert.de/PUB/EvertHardie2011.pdf>). The 'cwbtools'
package offers pure R tools to create indexed corpus files as well as
high-level wrappers for the original C implementation of CWB as exposed by
the 'RcppCWB' package <https://CRAN.R-project.org/package=RcppCWB>.
Additional functionality to add and modify annotations of corpora from
within R makes working with CWB indexed corpora much more flexible and
convenient. The 'cwbtools' package in combination with the R packages
'RcppCWB' (<https://CRAN.R-project.org/package=RcppCWB>) and 'polmineR'
(<https://CRAN.R-project.org/package=polmineR>) offers a lightweight
infrastructure to support the combination of quantitative and qualitative
approaches for working with textual data.

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
