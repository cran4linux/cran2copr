%global __brp_check_rpaths %{nil}
%global packname  findR
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          3%{?dist}%{?buildtag}
Summary:          Find Code Snippets, R Scripts, R Markdown, PDF and Text Fileswith Pattern Matching

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-pdftools 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-pdftools 
Requires:         R-CRAN-stringr 

%description
Scans all directories and subdirectories of a path for code snippets, R
scripts, R Markdown, PDF or text files containing a specific pattern.
Files found can be copied to a new folder.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
