%global packname  udunits2
%global packver   0.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.13
Release:          2%{?dist}
Summary:          Udunits-2 Bindings for R

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    udunits2-devel
Requires:         udunits2
BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0

%description
Provides simple bindings to Unidata's udunits library.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}\
  --configure-args='--with-udunits2-include=/usr/include/udunits2'
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
%doc %{rlibdir}/%{packname}/share
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
