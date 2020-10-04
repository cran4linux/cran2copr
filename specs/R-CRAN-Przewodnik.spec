%global packname  Przewodnik
%global packver   0.16.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.16.12
Release:          3%{?dist}%{?buildtag}
Summary:          Datasets and Functions Used in the Book 'Przewodnik po PakiecieR'

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-PogromcyDanych 
BuildRequires:    R-CRAN-PBImisc 
Requires:         R-CRAN-PogromcyDanych 
Requires:         R-CRAN-PBImisc 

%description
Data sets and functions used in the polish book "Przewodnik po pakiecie R"
(The Hitchhiker's Guide to the R). See more at <http://biecek.pl/R>. Among
others you will find here data about housing prices, cancer patients,
running times and many others.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
