%global packname  ipfr
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          List Balancing for Reweighting and Population Synthesis

License:          Apache License (== 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-mlr >= 2.11
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-dplyr >= 0.7.3
BuildRequires:    R-CRAN-tidyr >= 0.5.1
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-mlr >= 2.11
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-dplyr >= 0.7.3
Requires:         R-CRAN-tidyr >= 0.5.1

%description
Performs iterative proportional updating given a seed table and an
arbitrary number of marginal distributions. This is commonly used in
population synthesis, survey raking, matrix rebalancing, and other
applications. For example, a household survey may be weighted to match the
known distribution of households by size from the census. An origin/
destination trip matrix might be balanced to match traffic counts. The
approach used by this package is based on a paper from Arizona State
University (Ye, Xin, et. al. (2009)
<http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.537.723&rep=rep1&type=pdf>).
Some enhancements have been made to their work including primary and
secondary target balance/importance, general marginal agreement, and
weight restriction.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
