%global packname  fExpressCertificates
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          2%{?dist}
Summary:          Structured Products Valuation forExpressCertificates/Autocallables

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tmvtnorm 
BuildRequires:    R-CRAN-fCertificates 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-fExoticOptions 
BuildRequires:    R-CRAN-fOptions 
Requires:         R-CRAN-tmvtnorm 
Requires:         R-CRAN-fCertificates 
Requires:         R-CRAN-mvtnorm 
Requires:         R-Matrix 
Requires:         R-CRAN-fExoticOptions 
Requires:         R-CRAN-fOptions 

%description
Provides pricing by duplication and Monte Carlo methods for Express
Certificates products (also known as Autocallables).

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
