%global __brp_check_rpaths %{nil}
%global packname  asympTest
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          3%{?dist}%{?buildtag}
Summary:          A Simple R Package for Classical Parametric Statistical Testsand Confidence Intervals in Large Samples

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 1.8.0
Requires:         R-core >= 1.8.0
BuildArch:        noarch

%description
One and two sample mean and variance tests (differences and ratios) are
considered. The test statistics are all expressed in the same form as the
Student t-test, which facilitates their presentation in the classroom.
This contribution also fills the gap of a robust (to non-normality)
alternative to the chi-square single variance test for large samples,
since no such procedure is implemented in standard statistical software.

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
