%global packname  rsyntax
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Extract Semantic Relations from Text by Querying and ReshapingSyntax

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.11.8
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tokenbrowser 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-png 
Requires:         R-CRAN-data.table >= 1.11.8
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-tidyselect 
Requires:         R-methods 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tokenbrowser 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-png 

%description
Various functions for querying and reshaping dependency trees, as for
instance created with the 'spacyr' or 'udpipe' packages. This enables the
automatic extraction of useful semantic relations from texts, such as
quotes (who said what) and clauses (who did what). Method proposed in Van
Atteveldt et al. (2017) <doi:10.1017/pan.2016.12>.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
