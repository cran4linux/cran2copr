%global __brp_check_rpaths %{nil}
%global packname  ionr
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          2%{?dist}%{?buildtag}
Summary:          Test for Indifference of Indicator

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-psych 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-psych 

%description
Provides item exclusion procedure, which is a formal method to test
'Indifference Of iNdicator' (ION). When a latent personality trait-outcome
association is assumed, then the association strength should not depend on
which subset of indicators (i.e. items) has been chosen to reflect the
trait. Personality traits are often measured (reflected) by a sum-score of
a certain set of indicators. Item exclusion procedure randomly excludes
items from a sum-score and tests, whether the sum-score - outcome
correlation changes. ION has been achieved, when any item can be excluded
from the sum-score without the sum-score - outcome correlation
substantially changing . For more details, see Vainik, Mottus et. al,
(2015) "Are Trait-Outcome Associations Caused by Scales or Particular
Items? Example Analysis of Personality Facets and BMI",European Journal of
Personality DOI: <10.1002/per.2009> .

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

%files
%{rlibdir}/%{packname}
