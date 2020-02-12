%global packname  natmanager
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Install the 'Natverse' Packages from Scratch

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-gh 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-remotes 
BuildRequires:    R-CRAN-usethis 
Requires:         R-CRAN-gh 
Requires:         R-utils 
Requires:         R-CRAN-remotes 
Requires:         R-CRAN-usethis 

%description
Enables user to install different packages in the 'natverse' repository
from scratch. The rationale behind the utility of this package is as
follows. The suite of packages encompassed by 'natverse' helps in
analysing neuroanatomical data ranging from a variety of species like the
nematode worm to the mouse brain. The principal problem while installing
the core 'natverse' package is that it installs a lot of its friends
(dependencies, imports etc.) that are required for its proper functioning.
Most of these friends are development packages (which are also quite
heavy) located in GITHUB. This in turn makes the installation of
'natverse' to have a lot of API calls to the GITHUB, however GITHUB has a
limit of 60 requests per hour for unauthenticated requests. Hence for the
unauthenticated user, the installation would fail if it was done directly.
The proper way to fix this problem would be to set the GITHUB_PAT to make
the request authenticated. Hence, to make the installation of 'natverse'
easier from the end user perspective (who are not well versed in R or in
GITHUB), we have developed this package. This package will act as a
wrapper that will set the GITHUB_PAT and will handhold the user to
initiate the installation of the 'natverse' packages.

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
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
