%global packname  gistr
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          3%{?dist}
Summary:          Work with 'GitHub' 'Gists'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.4
BuildRequires:    R-CRAN-httr >= 1.2.0
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-jsonlite >= 1.4
Requires:         R-CRAN-httr >= 1.2.0
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-dplyr 

%description
Work with 'GitHub' 'gists' from 'R' (e.g.,
<http://en.wikipedia.org/wiki/GitHub#Gist>,
<https://help.github.com/articles/about-gists/>). A 'gist' is simply one
or more files with code/text/images/etc. This package allows the user to
create new 'gists', update 'gists' with new files, rename files, delete
files, get and delete 'gists', star and 'un-star' 'gists', fork 'gists',
open a 'gist' in your default browser, get embed code for a 'gist', list
'gist' 'commits', and get rate limit information when 'authenticated'.
Some requests require authentication and some do not. 'Gists' website:
<https://gist.github.com/>.

%prep
%setup -q -c -n %{packname}


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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/ignore
%doc %{rlibdir}/%{packname}/img
%doc %{rlibdir}/%{packname}/vign
%{rlibdir}/%{packname}/INDEX
