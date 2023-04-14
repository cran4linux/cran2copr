%global __brp_check_rpaths %{nil}
%global packname  citecorp
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          3%{?dist}%{?buildtag}
Summary:          Client for the Open Citations Corpus

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-crul >= 0.7.0
BuildRequires:    R-CRAN-fauxpas >= 0.5.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-crul >= 0.7.0
Requires:         R-CRAN-fauxpas >= 0.5.0
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-jsonlite 

%description
Client for the Open Citations Corpus (<http://opencitations.net/>).
Includes a set of functions for getting one identifier type from another,
as well as getting references and citations for a given identifier.

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
