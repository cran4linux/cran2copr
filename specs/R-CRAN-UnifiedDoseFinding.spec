%global packname  UnifiedDoseFinding
%global packver   0.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Dose-Finding Methods for Non-Binary Outcomes

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
In many phase I trials, the design goal is to find the dose associated
with a certain target toxicity rate. In some trials, the goal can be to
find the dose with a certain weighted sum of rates of various toxicity
grades. For others, the goal is to find the dose with a certain mean value
of a continuous response. This package provides the setup and calculations
needed to run a dose-finding trial with non-binary endpoints and performs
simulations to assess design’s operating characteristics under various
scenarios. Three dose finding designs are included in this package:
unified phase I design (Ivanova et al. (2009)
<doi:10.1111/j.1541-0420.2008.01045.x>), Quasi-CRM/Robust-Quasi-CRM (Yuan
et al. (2007) <doi:10.1111/j.1541-0420.2006.00666.x>, Pan et al. (2014)
<doi:10.1371/journal.pone.0098147>) and generalized BOIN design (Mu et al.
(2018) <doi:10.1111/rssc.12263>). The toxicity endpoints can be handled
with these functions including equivalent toxicity score (ETS), total
toxicity burden (TTB), general continuous toxicity endpoints, with
incorporating ordinal grade toxicity information into dose-finding
procedure. These functions allow customization of design characteristics
to vary sample size, cohort sizes, target dose-limiting toxicity (DLT)
rates, discrete or continuous toxicity score, and incorporate safety
and/or stopping rules.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
