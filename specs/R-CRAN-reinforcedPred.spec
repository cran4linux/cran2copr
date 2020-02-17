%global packname  reinforcedPred
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Reinforced Risk Prediction with Budget Constraint

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3.50
BuildRequires:    R-CRAN-glmnet >= 2.0.16
BuildRequires:    R-CRAN-refund >= 0.1.17
BuildRequires:    R-stats 
Requires:         R-MASS >= 7.3.50
Requires:         R-CRAN-glmnet >= 2.0.16
Requires:         R-CRAN-refund >= 0.1.17
Requires:         R-stats 

%description
Traditional risk prediction only utilizes baseline factors known to be
associated with the disease. Given that longitudinal information are
routinely measured and documented for patients, it is worthwhile to make
full use of these data. The available longitudinal biomarker data will
likely improve prediction. However, repeated biomarker collection could be
costly and inconvenient, and risk prediction for patients at a later time
could delay necessary medical decisions. Thus, there is a trade-off
between high quality prediction and cost. This package implements a
cost-effective statistical procedure that recursively incorporates
comprehensive longitudinal information into the risk prediction model,
taking into account the cost of delaying the decision to a follow-up time
when more information is available. The statistical methods are described
in the following paper: Pan, Y., Laber, E., Smith, M., Zhao, Y. (2018).
Reinforced risk prediction with budget constraint: application to
electronic health records data. Manuscript submitted for publication.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
