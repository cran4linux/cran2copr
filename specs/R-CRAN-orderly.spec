%global packname  orderly
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Lightweight Reproducible Reporting

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-zip >= 2.0.0
BuildRequires:    R-CRAN-fs >= 1.2.7
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-docopt 
BuildRequires:    R-CRAN-ids 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-zip >= 2.0.0
Requires:         R-CRAN-fs >= 1.2.7
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-docopt 
Requires:         R-CRAN-ids 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-yaml 

%description
Order, create and store reports from R.  By defining a lightweight
interface around the inputs and outputs of an analysis, a lot of the
repetitive work for reproducible research can be automated.  We define a
simple format for organising and describing work that facilitates
collaborative reproducible research and acknowledges that all analyses are
run multiple times over their lifespans.

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
%doc %{rlibdir}/%{packname}/create_orderly_demo.sh
%{rlibdir}/%{packname}/database
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/init
%doc %{rlibdir}/%{packname}/migrate
%doc %{rlibdir}/%{packname}/script
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
