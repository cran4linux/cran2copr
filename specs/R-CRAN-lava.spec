%global packname  lava
%global packver   1.6.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.7
Release:          3%{?dist}
Summary:          Latent Variable Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-stats 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-SQUAREM 
BuildRequires:    R-utils 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-numDeriv 
Requires:         R-stats 
Requires:         R-survival 
Requires:         R-CRAN-SQUAREM 
Requires:         R-utils 

%description
A general implementation of Structural Equation Models with latent
variables (MLE, 2SLS, and composite likelihood estimators) with both
continuous, censored, and ordinal outcomes (Holst and Budtz-Joergensen
(2013) <doi:10.1007/s00180-012-0344-y>). Mixture latent variable models
and non-linear latent variable models (Holst and Budtz-Joergensen (2019)
<doi:10.1093/biostatistics/kxy082>). The package also provides methods for
graph exploration (d-separation, back-door criterion), simulation of
general non-linear latent variable models, and estimation of influence
functions for a broad range of statistical models.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/gof1.png
%doc %{rlibdir}/%{packname}/lava1.png
%doc %{rlibdir}/%{packname}/me1.png
%doc %{rlibdir}/%{packname}/mediation1.png
%doc %{rlibdir}/%{packname}/mediation2.png
%{rlibdir}/%{packname}/INDEX
