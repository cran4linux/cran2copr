%global __brp_check_rpaths %{nil}
%global packname  MargCond
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Joint Marginal-Conditional Model

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-gee 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-gee 
Requires:         R-CRAN-lme4 
Requires:         R-MASS 
Requires:         R-Matrix 

%description
Fits joint marginal conditional models for multivariate longitudinal data,
as in Proudfoot, Faig, Natarajan, and Xu (2018) <doi:10.1002/sim.7552>.
Development of this package was supported by the UCSD Altman Translational
Research Institute, NIH grant UL1TR001442. The content is solely the
responsibility of the authors and does not necessarily represent the
official views of the NIH.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
