%global packname  genpathmox
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          1%{?dist}
Summary:          Generalized Pathmox Approach Segmentation Tree Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-diagram 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-plspm 
BuildRequires:    R-CRAN-quantreg 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-CRAN-diagram 
Requires:         R-methods 
Requires:         R-CRAN-mice 
Requires:         R-CRAN-plspm 
Requires:         R-CRAN-quantreg 

%description
Provides a very interesting solution for handling segmentation variables
in complex statistical methodology. It contains en extended version of the
"Pathmox" algorithm (Lamberti, Sanchez and
Aluja,(2016)<doi:10.1002/asmb.2168>) in the context of Partial Least
Squares Path Modeling including the F-block test (to detect the
responsible latent endogenous equations of the difference), the
F-coefficient (to detect the path coefficients responsible of the
difference) and the "invariance" test (to realize a comparison between the
sub-models' latent variables). Furthermore, the package contains a
generalized version of the "Pathmox" algorithm to approach different
methodologies: linear regression and least absolute regression models.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
