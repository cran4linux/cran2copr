%global packname  KappaV
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          3%{?dist}%{?buildtag}
Summary:          Calculates "vectorial Kappa", an index of congruence betweenpatchy mosaics.

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-PresenceAbsence 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-sp 
Requires:         R-CRAN-PresenceAbsence 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-sp 

%description
this package allows to quantify the congruence between two patchy mosaics
or landscapes. This "vectorial Kappa" approach extends the principle of
Cohen's Kappa index by calculating areas of intersected patches between
two mosaics rather than agreement between pixels. It provides an exact
alternative for patchy mosaics when a Kappa index is needed.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
