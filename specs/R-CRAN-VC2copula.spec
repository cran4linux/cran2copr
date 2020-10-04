%global packname  VC2copula
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Extend the 'copula' Package with Families and Models from'VineCopula'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-VineCopula >= 2.3.0
BuildRequires:    R-CRAN-copula >= 0.999.19.1
BuildRequires:    R-methods 
Requires:         R-CRAN-VineCopula >= 2.3.0
Requires:         R-CRAN-copula >= 0.999.19.1
Requires:         R-methods 

%description
Provides new classes for (rotated) BB1, BB6, BB7, BB8, and Tawn copulas,
extends the existing Gumbel and Clayton families with rotations, and
allows to set up a vine copula model using the 'copula' API. Corresponding
objects from the 'VineCopula' API can easily be converted.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
