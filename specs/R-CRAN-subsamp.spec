%global packname  subsamp
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Subsample Winner Algorithm for Variable Selection in LinearRegression with a Large Number of Variables

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch

%description
This subsample winner algorithm (SWA) for regression with a large-p data
(X, Y) selects the important variables (or features) among the p features
X in explaining the response Y.  The SWA first uses a base procedure, here
a linear regression, on each of subsamples randomly drawn from the p
variables, and then computes the scores of all features, i.e., the p
variables, according to the performance of these features collected in
each of the subsample analyses. It then obtains the 'semifinalist' of the
features based on the resulting scores and determines the 'finalists',
i.e., the important features, from the 'semifinalist'.  Fan, Sun and Qiao
(2017) <http://sr2c.case.edu/swa-reg/>.

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
%{rlibdir}/%{packname}/INDEX
