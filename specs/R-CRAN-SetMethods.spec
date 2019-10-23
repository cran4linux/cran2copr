%global packname  SetMethods
%global packver   2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4
Release:          1%{?dist}
Summary:          Functions for Set-Theoretic Multi-Method Research and AdvancedQCA

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-QCA 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-betareg 
BuildRequires:    R-CRAN-fmsb 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-scatterplot3d 
Requires:         R-CRAN-QCA 
Requires:         R-methods 
Requires:         R-CRAN-betareg 
Requires:         R-CRAN-fmsb 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-lattice 
Requires:         R-CRAN-scatterplot3d 

%description
Functions for performing set-theoretic multi-method research, QCA for
clustered data, theory evaluation, Enhanced Standard Analysis, indirect
calibration, radar visualisations. Additionally it includes data to
replicate the examples in the book by C. Q. Schneider and C. Wagemann "Set
Theoretic Methods for the Social Sciences", Cambridge University Press and
in the online appendix.

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
%{rlibdir}/%{packname}/INDEX
