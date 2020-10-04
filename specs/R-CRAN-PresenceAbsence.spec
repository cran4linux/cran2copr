%global packname  PresenceAbsence
%global packver   1.1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.9
Release:          3%{?dist}%{?buildtag}
Summary:          Presence-Absence Model Evaluation.

License:          Unlimited
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.2.0
Requires:         R-core >= 2.2.0
BuildArch:        noarch

%description
This package provides a set of functions useful when evaluating the
results of presence-absence models. Package includes functions for
calculating threshold dependent measures such as confusion matrices, pcc,
sensitivity, specificity, and Kappa, and produces plots of each measure as
the threshold is varied. It will calculate optimal threshold choice
according to a choice of optimization criteria. It also includes functions
to plot the threshold independent ROC curves along with the associated AUC
(area under the curve).

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CHANGELOG
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
