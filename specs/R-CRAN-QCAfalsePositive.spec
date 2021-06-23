%global __brp_check_rpaths %{nil}
%global packname  QCAfalsePositive
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Tests for Type I Error in Qualitative Comparative Analysis (QCA)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch

%description
Implements tests for Type I error in Qualitative Comparative Analysis
(QCA) that take into account the multiple hypothesis tests inherent in the
procedure. Tests can be carried out on three variants of QCA: crisp-set
QCA (csQCA), multi-value QCA (mvQCA) and fuzzy-set QCA (fsQCA). For fsQCA,
the fsQCApermTest() command implements a permutation test that provides
95% confidence intervals for the number of counterexamples and degree of
consistency, respectively. The distributions of permuted values can be
plotted against the observed values. For csQCA and mvQCA, simple binomial
tests are implemented in csQCAbinTest() and mvQCAbinTest(), respectively.

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
