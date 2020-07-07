%global packname  micEconSNQP
%global packver   0.6-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.8
Release:          3%{?dist}
Summary:          Symmetric Normalized Quadratic Profit Function

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.4.0
Requires:         R-core >= 2.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-systemfit >= 1.0.0
BuildRequires:    R-CRAN-miscTools >= 0.6.1
BuildRequires:    R-MASS 
Requires:         R-CRAN-systemfit >= 1.0.0
Requires:         R-CRAN-miscTools >= 0.6.1
Requires:         R-MASS 

%description
Tools for econometric production analysis with the Symmetric Normalized
Quadratic (SNQ) profit function, e.g. estimation, imposing convexity in
prices, and calculating elasticities and shadow prices.

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
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
