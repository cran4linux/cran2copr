%global __brp_check_rpaths %{nil}
%global packname  costsensitive
%global packver   0.1.2.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2.10
Release:          3%{?dist}%{?buildtag}
Summary:          Cost-Sensitive Multi-Class Classification

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core

%description
Reduction-based techniques for cost-sensitive multi-class classification,
in which each observation has a different cost for classifying it into one
class, and the goal is to predict the class with the minimum expected cost
for each new observation. Implements Weighted All-Pairs (Beygelzimer, A.,
Langford, J., & Zadrozny, B., 2008, <doi:10.1007/978-0-387-79361-0_1>),
Weighted One-Vs-Rest (Beygelzimer, A., Dani, V., Hayes, T., Langford, J.,
& Zadrozny, B., 2005, <https://dl.acm.org/citation.cfm?id=1102358>) and
Regression One-Vs-Rest. Works with arbitrary classifiers taking
observation weights, or with regressors. Also implements
cost-proportionate rejection sampling for working with classifiers that
don't accept observation weights.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
