%global packname  exact2x2
%global packver   1.6.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.4.1
Release:          1%{?dist}
Summary:          Exact Tests and Confidence Intervals for 2x2 Tables

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats >= 3.1.1
BuildRequires:    R-CRAN-exactci 
BuildRequires:    R-CRAN-ssanv 
Requires:         R-stats >= 3.1.1
Requires:         R-CRAN-exactci 
Requires:         R-CRAN-ssanv 

%description
Calculates conditional exact tests (Fisher's exact test, Blaker's exact
test, or exact McNemar's test) and unconditional exact tests (including
score-based tests on differences in proportions, ratios of proportions,
and odds ratios, and Boshcloo's test) with appropriate matching confidence
intervals, and provides power and sample size calculations. Gives melded
confidence intervals for the binomial case (Fay, et al, 2015,
<DOI:10.1111/biom.12231>). Gives boundary-optimized rejection region test
(Gabriel, et al, 2018, <DOI:10.1002/sim.7579>), an unconditional exact
test for the situation where the controls are all expected to fail.

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
