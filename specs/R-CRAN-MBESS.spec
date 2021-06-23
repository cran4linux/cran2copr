%global __brp_check_rpaths %{nil}
%global packname  MBESS
%global packver   4.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.8.0
Release:          1%{?dist}%{?buildtag}
Summary:          The MBESS R Package

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-gsl 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-OpenMx 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-sem 
BuildRequires:    R-CRAN-semTools 
Requires:         R-stats 
Requires:         R-boot 
Requires:         R-CRAN-gsl 
Requires:         R-CRAN-lavaan 
Requires:         R-MASS 
Requires:         R-methods 
Requires:         R-CRAN-mnormt 
Requires:         R-nlme 
Requires:         R-CRAN-OpenMx 
Requires:         R-parallel 
Requires:         R-CRAN-sem 
Requires:         R-CRAN-semTools 

%description
Implements methods that useful in designing research studies and analyzing
data, with particular emphasis on methods that are developed for or used
within the behavioral, educational, and social sciences (broadly defined).
That being said, many of the methods implemented within MBESS are
applicable to a wide variety of disciplines. MBESS has a suite of
functions for a variety of related topics, such as effect sizes,
confidence intervals for effect sizes (including standardized effect sizes
and noncentral effect sizes), sample size planning (from the accuracy in
parameter estimation [AIPE], power analytic, equivalence, and minimum-risk
point estimation perspectives), mediation analysis, various properties of
distributions, and a variety of utility functions. MBESS (pronounced
'em-bes') was originally an acronym for 'Methods for the Behavioral,
Educational, and Social Sciences,' but at this point MBESS contains
methods applicable and used in a wide variety of fields and is an orphan
acronym, in the sense that what was an acronym is now literally its name.
MBESS has greatly benefited from others, see
<http://nd.edu/~kkelley/site/MBESS.html> for a detailed list of those that
have contributed and other details.

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
