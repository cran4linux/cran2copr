%global __brp_check_rpaths %{nil}
%global packname  metaggR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate the Knowledge-Weighted Estimate

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-stats 

%description
According to a phenomenon known as "the wisdom of the crowds," combining
point estimates from multiple judges often provides a more accurate
aggregate estimate than using a point estimate from a single judge.
However, if the judges use shared information in their estimates, the
simple average will over-emphasize this common component at the expense of
the judges’ private information. Asa Palley & Ville Satopää (2021)
"Boosting the Wisdom of Crowds Within a Single Judgment Problem: Selective
Averaging Based on Peer Predictions"
<https://papers.ssrn.com/sol3/Papers.cfm?abstract_id=3504286> proposes a
procedure for calculating a weighted average of the judges’ individual
estimates such that resulting aggregate estimate appropriately combines
the judges' collective information within a single estimation problem. The
authors use both simulation and data from six experimental studies to
illustrate that the weighting procedure outperforms existing
averaging-like methods, such as the equally weighted average, trimmed
average, and median. This aggregate estimate -- know as "the
knowledge-weighted estimate" -- inputs a) judges' estimates of a
continuous outcome (E) and b) predictions of others' average estimate of
this outcome (P). In this R-package, the function
knowledge_weighted_estimate(E,P) implements the knowledge-weighted
estimate. Its use is illustrated with a simple stylized example and on
real-world experimental data.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
