%global packname  Disequilibrium
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Disequilibrium Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-optimr 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-CRAN-optimr 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-numDeriv 

%description
Estimate, summarize, and perform predictions with the market in
disequilibrium model, as found in Gourieroux, C. (2000)
<doi:10.1017/CBO9780511805608> and Maddala, G. (1983)
<doi:10.1017/CBO9780511810176>. The parameters are estimated with maximum
likelihood.

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
%{rlibdir}/%{packname}/INDEX
