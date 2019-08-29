%global packname  FrF2.catlg128
%global packver   1.2-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}
Summary:          Catalogues of resolution IV 128 run 2-level fractionalfactorials up to 33 factors that do have 5-letter words

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.13.0
Requires:         R-core >= 2.13.0
BuildArch:        noarch
BuildRequires:    R-CRAN-FrF2 >= 1.4
Requires:         R-CRAN-FrF2 >= 1.4

%description
This package provides catalogues of resolution IV regular fractional
factorial designs in 128 runs for up to 33 2-level factors. The catalogues
are complete, excluding resolution IV designs without 5-letter words,
because these do not add value for a search for clear designs. The
previous package version 1.0 with complete catalogues up to 24 runs (24
runs and a namespace added later) can be downloaded from the authors
website.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
