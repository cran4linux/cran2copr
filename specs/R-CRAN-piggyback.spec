%global packname  piggyback
%global packver   0.0.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.10
Release:          1%{?dist}
Summary:          Managing Larger Data on a GitHub Repository

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-gh 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-git2r 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-clisymbols 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-memoise 
Requires:         R-CRAN-gh 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-git2r 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-usethis 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-clisymbols 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-memoise 

%description
Because larger (> 50 MB) data files cannot easily be committed to git, a
different approach is required to manage data associated with an analysis
in a GitHub repository.  This package provides a simple work-around by
allowing larger (up to 2 GB) data files to piggyback on a repository as
assets attached to individual GitHub releases.  These files are not
handled by git in any way, but instead are uploaded, downloaded, or edited
directly by calls through the GitHub API. These data files can be
versioned manually by creating different releases.  This approach works
equally well with public or private repositories.  Data can be uploaded
and downloaded programmatically from scripts. No authentication is
required to download data from public repositories.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
