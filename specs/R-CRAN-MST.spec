%global packname  MST
%global packver   2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2
Release:          3%{?dist}
Summary:          Multivariate Survival Trees

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-survival 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-partykit 
BuildRequires:    R-stats 
Requires:         R-survival 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-MASS 
Requires:         R-CRAN-Formula 
Requires:         R-methods 
Requires:         R-CRAN-partykit 
Requires:         R-stats 

%description
Constructs trees for multivariate survival data using marginal and frailty
models. Grows, prunes, and selects the best-sized tree.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
