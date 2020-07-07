%global packname  MSPRT
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          3%{?dist}
Summary:          A Modified Sequential Probability Ratio Test (MSPRT)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-datasets 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-iterators 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-datasets 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
A modified SPRT (MSPRT) can be designed and implemented with the help of
this package. In a MSPRT design, (i) the maximum sample size of an
experiment is fixed prior to the start of an experiment; (ii) the
alternative hypothesis used to define the rejection region of the test is
derived from the size of the test (Type I error), the maximum available
sample size (N), and (iii) the targeted Type 2 error (equals to 1 minus
the power) is also prespecified. Given these values, the MSPRT is defined
in a manner very similar to Wald's initial proposal. This test can reduce
the average sample size required to perform statistical hypothesis tests
at the specified level of significance and power. This package implements
one-sample proportion tests, one-sample Z-tests, one-sample T-tests,
two-sample Z-tests and two-sample T-tests. A user guidance for this
package is provided here. One can also refer to the supplemental
information for the same.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
