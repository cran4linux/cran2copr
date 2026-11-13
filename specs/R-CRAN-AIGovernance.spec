%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AIGovernance
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Auditing, Drift Monitoring and Governance Reporting for AI Decision Systems

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-nnet 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-nnet 

%description
Provides statistical auditing, risk documentation, and reporting tools to
support AI governance workflows for employment, hiring and other
AI-assisted decision systems. Implements the EEOC four-fifths adverse
impact rule (Equal Employment Opportunity Commission, 1978,
<https://www.ecfr.gov/current/title-29/subtitle-B/chapter-XIV/part-1607>),
NYC Local Law 144 bias audit requirements (New York City, 2023,
<https://www.nyc.gov/site/dca/about/automated-employment-decision-tools.page>),
and the AI Risk Management Framework checklist items from the National
Institute of Standards and Technology (2023, <doi:10.6028/NIST.AI.100-1>).
Optionally supports EU AI Act high-risk classification (European
Parliament and Council, 2024,
<https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai>).
It also audits decision drift over time: the change in a decision rate is
decomposed into case-mix, allocation (routing of cases to decision units)
and rule-change components in the spirit of Kitagawa (1955)
<doi:10.1080/01621459.1955.10501299>; net and absolute drift are estimated
over a fixed reference case mix with overlap trimming and cluster
bootstrap uncertainty; categorical decisions and unit-level drift with
noise-corrected heterogeneity are supported; and a simulator with known
drift mechanisms is included. The package does not provide legal advice or
certify legal compliance; it is a statistical and documentation support
tool.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
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
