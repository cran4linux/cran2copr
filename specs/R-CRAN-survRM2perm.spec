%global packname  survRM2perm
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Permutation Test for Comparing Restricted Mean Survival Time

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-survival 
BuildRequires:    R-methods 
BuildRequires:    R-stats4 
Requires:         R-survival 
Requires:         R-methods 
Requires:         R-stats4 

%description
Performs the permutation test using difference in the restricted mean
survival time (RMST) between groups as a summary measure of the survival
time distribution. When the sample size is less than 50 per group, it has
been shown that there is non-negligible inflation of the type I error rate
in the commonly used asymptotic test for the RMST comparison. Generally,
permutation tests can be useful in such a situation. However, when we
apply the permutation test for the RMST comparison, particularly in small
sample situations, there are some cases where the survival function in
either group cannot be defined due to censoring in the permutation
process. Horiguchi and Uno (2020) <doi:10.1002/sim.8565> have examined six
workable solutions to handle this numerical issue. It performs permutation
tests with implementation of the six methods outlined in the paper when
the numerical issue arises during the permutation process. The result of
the asymptotic test is also provided for a reference.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
