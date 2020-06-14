%global packname  yum
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          2%{?dist}
Summary:          Utilities to Extract and Process 'YAML' Fragments

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-yaml >= 2.2
Requires:         R-CRAN-yaml >= 2.2

%description
Provides a number of functions to facilitate extracting information in
'YAML' fragments from one or multiple files, optionally structuring the
information in a 'data.tree'. 'YAML' (recursive acronym for "YAML ain't
Markup Language") is a convention for specifying structured data in a
format that is both machine- and human-readable. 'YAML' therefore lends
itself well for embedding (meta)data in plain text files, such as Markdown
files. This principle is implemented in 'yum' with minimal dependencies
(i.e. only the 'yaml' packages, and the 'data.tree' package can be used to
enable additional functionality).

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
