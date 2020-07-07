%global packname  micEconCES
%global packver   0.9-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.8
Release:          3%{?dist}
Summary:          Analysis with the Constant Elasticity of Substitution (CES)function

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.4.0
Requires:         R-core >= 2.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DEoptim >= 2.0.4
BuildRequires:    R-CRAN-car >= 2.0.0
BuildRequires:    R-CRAN-minpack.lm >= 1.1.4
BuildRequires:    R-CRAN-systemfit >= 1.0.0
BuildRequires:    R-CRAN-micEcon >= 0.6.1
BuildRequires:    R-CRAN-miscTools >= 0.6.1
Requires:         R-CRAN-DEoptim >= 2.0.4
Requires:         R-CRAN-car >= 2.0.0
Requires:         R-CRAN-minpack.lm >= 1.1.4
Requires:         R-CRAN-systemfit >= 1.0.0
Requires:         R-CRAN-micEcon >= 0.6.1
Requires:         R-CRAN-miscTools >= 0.6.1

%description
Tools for economic analysis and economic modelling with a Constant
Elasticity of Substitution (CES) function

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/Kemfert98Nest1GridLm.RData
%{rlibdir}/%{packname}/INDEX
