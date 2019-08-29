%global packname  catfun
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}
Summary:          Categorical Data Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-epitools 
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-epitools 
Requires:         R-CRAN-DescTools 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-rlang 

%description
Includes wrapper functions around existing functions for the analysis of
categorical data and introduces functions for calculating risk differences
and matched odds ratios. R currently supports a wide variety of tools for
the analysis of categorical data. However, many functions are spread
across a variety of packages with differing syntax and poor compatibility
with each another. prop_test() combines the functions binom.test(),
prop.test() and BinomCI() into one output. prop_power() allows for power
and sample size calculations for both balanced and unbalanced designs.
riskdiff() is used for calculating risk differences and matched_or() is
used for calculating matched odds ratios. For further information on
methods used that are not documented in other packages see Nathan Mantel
and William Haenszel (1959) <doi:10.1093/jnci/22.4.719> and Alan Agresti
(2002) <ISBN:0-471-36093-7>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
