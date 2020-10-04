%global packname  QTOCen
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Quantile-Optimal Treatment Regimes with Censored Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-rgenoud >= 5.8
BuildRequires:    R-CRAN-quantreg >= 5.18
BuildRequires:    R-utils 
BuildRequires:    R-survival 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-MatrixModels 
Requires:         R-CRAN-rgenoud >= 5.8
Requires:         R-CRAN-quantreg >= 5.18
Requires:         R-utils 
Requires:         R-survival 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-MatrixModels 

%description
Provides methods for estimation of mean- and quantile-optimal treatment
regimes from censored data. Specifically, we have developed distinct
functions for three types of right censoring for static treatment using
quantile criterion: (1) independent/random censoring, (2)
treatment-dependent random censoring, and (3) covariates-dependent random
censoring. It also includes a function to estimate quantile-optimal
dynamic treatment regimes for independent censored data. Finally, this
package also includes a simulation data generative model of a dynamic
treatment experiment proposed in literature.

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
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
