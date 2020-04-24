%global packname  HyRiM
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}
Summary:          Multicriteria Risk Management using Zero-Sum Games withVector-Valued Payoffs that are Probability Distributions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-compare 
BuildRequires:    R-CRAN-orthopolynom 
BuildRequires:    R-CRAN-grImport2 
BuildRequires:    R-CRAN-Rglpk 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-compare 
Requires:         R-CRAN-orthopolynom 
Requires:         R-CRAN-grImport2 
Requires:         R-CRAN-Rglpk 
Requires:         R-CRAN-purrr 

%description
Construction and analysis of multivalued zero-sum matrix games over the
abstract space of probability distributions, which describe the losses in
each scenario of defense vs. attack action. The distributions can be
compiled directly from expert opinions or other empirical data (insofar
available). The package implements the methods put forth in the EU project
HyRiM (Hybrid Risk Management for Utility Networks), FP7 EU Project Number
608090. The method has been published in Rass, S., König, S., Schauer, S.,
2016. Decisions with Uncertain Consequences-A Total Ordering on
Loss-Distributions. PLoS ONE 11, e0168583.
<doi:10.1371/journal.pone.0168583>, and applied for advanced persistent
thread modeling in Rass, S., König, S., Schauer, S., 2017. Defending
Against Advanced Persistent Threats Using Game-Theory. PLoS ONE 12,
e0168675. <doi:10.1371/journal.pone.0168675>. A volume covering the wider
range of aspects of risk management, partially based on the theory
implemented in the package is the book edited by S. Rass and S. Schauer,
2018. Game Theory for Security and Risk Management: From Theory to
Practice. Springer, <doi:10.1007/978-3-319-75268-6>, ISBN
978-3-319-75267-9.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
