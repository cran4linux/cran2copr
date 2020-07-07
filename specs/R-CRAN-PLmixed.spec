%global packname  PLmixed
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          3%{?dist}
Summary:          Estimate (Generalized) Linear Mixed Models with FactorStructures

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-Matrix >= 1.1.1
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-optimx 
Requires:         R-Matrix >= 1.1.1
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-numDeriv 
Requires:         R-stats 
Requires:         R-CRAN-optimx 

%description
Utilizes the 'lme4' and 'optimx' packages (previously the optim() function
from 'stats') to estimate (generalized) linear mixed models (GLMM) with
factor structures using a profile likelihood approach, as outlined in Jeon
and Rabe-Hesketh (2012) <doi:10.3102/1076998611417628> and Rockwood and
Jeon (2019) <doi:10.1080/00273171.2018.1516541>. Factor analysis and item
response models can be extended to allow for an arbitrary number of nested
and crossed random effects, making it useful for multilevel and
cross-classified models.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
