%global packname  CSMES
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}
Summary:          Cost-Sensitive Multi-Criteria Ensemble Selection for UncertainCost Conditions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-rpart >= 4.1.15
BuildRequires:    R-graphics >= 3.5.1
BuildRequires:    R-stats >= 3.5.1
BuildRequires:    R-CRAN-zoo >= 1.8.6
BuildRequires:    R-CRAN-caTools >= 1.18.0
BuildRequires:    R-CRAN-data.table >= 1.12.2
BuildRequires:    R-CRAN-ROCR >= 1.0.7
BuildRequires:    R-CRAN-mco >= 1.0.15.1
Requires:         R-rpart >= 4.1.15
Requires:         R-graphics >= 3.5.1
Requires:         R-stats >= 3.5.1
Requires:         R-CRAN-zoo >= 1.8.6
Requires:         R-CRAN-caTools >= 1.18.0
Requires:         R-CRAN-data.table >= 1.12.2
Requires:         R-CRAN-ROCR >= 1.0.7
Requires:         R-CRAN-mco >= 1.0.15.1

%description
Functions for cost-sensitive multi-criteria ensemble selection (CSMES) (as
described in De bock et al. (2020) <doi:10.1016/j.ejor.2020.01.052>) for
cost-sensitive learning under unknown cost conditions.

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
