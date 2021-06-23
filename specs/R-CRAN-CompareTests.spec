%global __brp_check_rpaths %{nil}
%global packname  CompareTests
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Correct for Verification Bias in Diagnostic Accuracy & Agreement

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
A standard test is observed on all specimens.  We treat the second test
(or sampled test) as being conducted on only a stratified sample of
specimens.  Verification Bias is this situation when the specimens for
doing the second (sampled) test is not under investigator control.  We
treat the total sample as stratified two-phase sampling and use inverse
probability weighting.  We estimate diagnostic accuracy (category-specific
classification probabilities; for binary tests reduces to specificity and
sensitivity, and also predictive values) and agreement statistics (percent
agreement, percent agreement by category, Kappa (unweighted), Kappa
(quadratic weighted) and symmetry tests (reduces to McNemar's test for
binary tests)).  See: Katki HA, Li Y, Edelstein DW, Castle PE.  Estimating
the agreement and diagnostic accuracy of two diagnostic tests when one
test is conducted on only a subsample of specimens. Stat Med. 2012 Feb 28;
31(5) <doi:10.1002/sim.4422>.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
