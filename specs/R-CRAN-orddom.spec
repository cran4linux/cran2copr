%global packname  orddom
%global packver   3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1
Release:          1%{?dist}
Summary:          Ordinal Dominance Statistics

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-psych 
Requires:         R-CRAN-psych 

%description
Computes ordinal, statistics and effect sizes as an alternative to mean
comparison: Cliff's delta or success rate difference (SRD), Vargha and
Delaney's A or the Area Under a Receiver Operating Characteristic Curve
(AUC), the discrete type of McGraw & Wong's Common Language Effect Size
(CLES) or Grissom & Kim's Probability of Superiority (PS), and the Number
needed to treat (NNT) effect size. Moreover, comparisons to Cohen's d are
offered based on Huberty & Lowman's Percentage of Group (Non-)Overlap
considerations.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
