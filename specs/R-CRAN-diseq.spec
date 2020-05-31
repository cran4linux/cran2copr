%global packname  diseq
%global packver   0.0.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.11
Release:          1%{?dist}
Summary:          Estimation Methods for Markets in Disequilibrium

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3.50
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-tibble >= 1.4.2
BuildRequires:    R-CRAN-systemfit >= 1.1
BuildRequires:    R-CRAN-bbmle >= 1.0.20
BuildRequires:    R-CRAN-tidyr >= 1.0.2
BuildRequires:    R-CRAN-dplyr >= 0.7.6
BuildRequires:    R-CRAN-rlang >= 0.2.1
BuildRequires:    R-methods 
Requires:         R-MASS >= 7.3.50
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-tibble >= 1.4.2
Requires:         R-CRAN-systemfit >= 1.1
Requires:         R-CRAN-bbmle >= 1.0.20
Requires:         R-CRAN-tidyr >= 1.0.2
Requires:         R-CRAN-dplyr >= 0.7.6
Requires:         R-CRAN-rlang >= 0.2.1
Requires:         R-methods 

%description
Provides estimation methods for markets in equilibrium and disequilibrium.
Specifically, it supports the estimation of an equilibrium and four
disequilibrium models with both correlated and independent shocks. It also
provides post-estimation analysis tools, such as aggregation and marginal
effects calculations. The estimation methods are based on full information
maximum likelihood techniques given in Maddala and Nelson (1974)
<doi:10.2307/1914215>. They are implemented using the analytic derivative
expressions calculated in Karapanagiotis (2020)
<doi:10.2139/ssrn.3525622>. The equilibrium estimation constitutes a
special case of a system of simultaneous equations. The disequilibrium
models, instead, replace the market clearing condition with a short side
rule and allow for different specifications of price dynamics.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX