%global packname  yamlet
%global packver   0.4.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.7
Release:          2%{?dist}
Summary:          Versatile Curation of Table Metadata

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 0.8.1
BuildRequires:    R-CRAN-csv >= 0.5.4
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-encode 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-CRAN-spork 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-xtable 
Requires:         R-CRAN-dplyr >= 0.8.1
Requires:         R-CRAN-csv >= 0.5.4
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-encode 
Requires:         R-CRAN-units 
Requires:         R-CRAN-spork 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-xtable 

%description
The 'yamlet' package implements a file-based mechanism for documenting
datasets. It reads and writes YAML-formatted metadata and applies it as
data item attributes. Data and metadata are stored independently but can
be coordinated by using similar file paths with different extensions.  The
'yamlet' dialect is valid 'YAML', but some conventions are chosen to
improve readability. Defaults and conventions can be over-ridden by the
user. See ?yamlet and ?decorate.data.frame. See ?read_yamlet
?write_yamlet, and ?io_csv.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
