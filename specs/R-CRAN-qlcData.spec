%global packname  qlcData
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}
Summary:          Processing Data for Quantitative Language Comparison (QLC)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-yaml >= 2.1.11
BuildRequires:    R-CRAN-stringi >= 0.2.5
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-docopt 
BuildRequires:    R-CRAN-data.tree 
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-CRAN-ape 
Requires:         R-CRAN-yaml >= 2.1.11
Requires:         R-CRAN-stringi >= 0.2.5
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-docopt 
Requires:         R-CRAN-data.tree 
Requires:         R-CRAN-phytools 
Requires:         R-CRAN-ape 

%description
This is a collection of functions to read, recode, and transcode data for
QLC.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/exec
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/shiny
%{rlibdir}/%{packname}/INDEX
