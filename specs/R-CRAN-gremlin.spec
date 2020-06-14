%global packname  gremlin
%global packver   0.1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0.1
Release:          2%{?dist}
Summary:          Mixed-Effects REML Incorporating Generalized Inverses

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
Requires:         R-Matrix 
Requires:         R-methods 

%description
Fit linear mixed-effects models using restricted (or residual) maximum
likelihood (REML) and with generalized inverse matrices to specify
covariance structures for random effects. In particular, the package is
suited to fit quantitative genetic mixed models, often referred to as
'animal models' (Kruuk. 2004 <DOI: 10.1098/rstb.2003.1437>). Implements
the average information algorithm as the main tool to maximize the
restricted likelihood, but with other algorithms available (Meyer. 1997.
Genet Sel Evol 29:97; Meyer and Smith. 1998. Genet Sel Evol 28:23.).

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
