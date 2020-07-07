%global packname  pairwiseComparisons
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          2%{?dist}
Summary:          Multiple Pairwise Comparison Tests

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ipmisc >= 3.0.1
BuildRequires:    R-CRAN-WRS2 >= 1.1.0
BuildRequires:    R-CRAN-tidyBF >= 0.2.1
BuildRequires:    R-CRAN-broomExtra 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-dunn.test 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-PMCMRplus 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
Requires:         R-CRAN-ipmisc >= 3.0.1
Requires:         R-CRAN-WRS2 >= 1.1.0
Requires:         R-CRAN-tidyBF >= 0.2.1
Requires:         R-CRAN-broomExtra 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-dunn.test 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-PMCMRplus 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 

%description
Multiple pairwise comparison tests on tidy data for one-way analysis of
variance for both between-subjects and within-subjects designs. Currently,
it supports only the most common types of statistical analyses and tests:
parametric (Welch's and Student's t-test), nonparametric (Durbin-Conover
and Dunn test), robust (Yuen’s trimmed means test), and Bayes Factor
(Student's t-test).

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
