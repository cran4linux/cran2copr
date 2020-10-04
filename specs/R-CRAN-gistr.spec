%global packname  gistr
%global packver   0.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0
Release:          1%{?dist}%{?buildtag}
Summary:          Work with 'GitHub' 'Gists'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-crul 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-crul 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-dplyr 

%description
Work with 'GitHub' 'gists' from 'R' (e.g.,
<https://en.wikipedia.org/wiki/GitHub#Gist>,
<https://docs.github.com/en/github/writing-on-github/creating-gists/>). A
'gist' is simply one or more files with code/text/images/etc. This package
allows the user to create new 'gists', update 'gists' with new files,
rename files, delete files, get and delete 'gists', star and 'un-star'
'gists', fork 'gists', open a 'gist' in your default browser, get embed
code for a 'gist', list 'gist' 'commits', and get rate limit information
when 'authenticated'. Some requests require authentication and some do
not. 'Gists' website: <https://gist.github.com/>.

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
