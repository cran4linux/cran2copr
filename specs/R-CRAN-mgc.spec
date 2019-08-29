%global packname  mgc
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Multiscale Graph Correlation

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-SDMTools 
BuildRequires:    R-MASS 
Requires:         R-stats 
Requires:         R-CRAN-SDMTools 
Requires:         R-MASS 

%description
Multiscale Graph Correlation (MGC) is a framework developed by Shen et al.
(2017) <arXiv:1609.05148> that extends global correlation procedures to be
multiscale; consequently, MGC tests typically require far fewer samples
than existing methods for a wide variety of dependence structures and
dimensionalities, while maintaining computational efficiency. Moreover,
MGC provides a simple and elegant multiscale characterization of the
potentially complex latent geometry underlying the relationship.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
