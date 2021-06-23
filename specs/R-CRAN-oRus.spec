%global __brp_check_rpaths %{nil}
%global packname  oRus
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Operational Research User Stories

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tm 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidytext 
BuildRequires:    R-CRAN-topicmodels 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-xlsx 
BuildRequires:    R-CRAN-knitr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tm 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidytext 
Requires:         R-CRAN-topicmodels 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-xlsx 
Requires:         R-CRAN-knitr 

%description
A first implementation of automated parsing of user stories, when used to
defined functional requirements for operational research mathematical
models. It allows reading user stories, splitting them on the who-what-why
template, and classifying them according to the parts of the mathematical
model that they represent. Also provides semantic grouping of stories, for
project management purposes.

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
