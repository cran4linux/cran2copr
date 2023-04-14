%global __brp_check_rpaths %{nil}
%global packname  averisk
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          3%{?dist}%{?buildtag}
Summary:          Calculation of Average Population Attributable Fractions andConfidence Intervals

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3.0
Requires:         R-MASS >= 7.3.0

%description
Average population attributable fractions are calculated for a set of risk
factors (either binary or ordinal valued) for both prospective and case-
control designs. Confidence intervals are found by Monte Carlo simulation.
The method can be applied to either prospective or case control designs,
provided an estimate of disease prevalence is provided. In addition to an
exact calculation of AF, an approximate calculation, based on randomly
sampling permutations has been implemented to ensure the calculation is
computationally tractable when the number of risk factors is large.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
