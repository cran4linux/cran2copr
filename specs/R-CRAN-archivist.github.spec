%global __brp_check_rpaths %{nil}
%global packname  archivist.github
%global packver   0.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.6
Release:          3%{?dist}%{?buildtag}
Summary:          Tools for Archiving, Managing and Sharing R Objects via GitHub

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-archivist 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-git2r 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-digest 
Requires:         R-CRAN-archivist 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-git2r 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-digest 

%description
The extension of the 'archivist' package integrating the archivist with
GitHub via GitHub API, 'git2r' packages and 'httr' package.

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
%{rlibdir}/%{packname}
