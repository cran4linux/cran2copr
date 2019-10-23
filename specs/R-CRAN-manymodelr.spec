%global packname  manymodelr
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}
Summary:          Build and Tune Several Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-caret >= 6.0.81
BuildRequires:    R-CRAN-tibble >= 2.0.1
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-e1071 >= 1.7.0.1
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-reshape2 >= 1.4.3
BuildRequires:    R-CRAN-dplyr >= 0.7.8
BuildRequires:    R-CRAN-purrr >= 0.3.2
BuildRequires:    R-CRAN-Metrics >= 0.1.4
Requires:         R-CRAN-caret >= 6.0.81
Requires:         R-CRAN-tibble >= 2.0.1
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-e1071 >= 1.7.0.1
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-reshape2 >= 1.4.3
Requires:         R-CRAN-dplyr >= 0.7.8
Requires:         R-CRAN-purrr >= 0.3.2
Requires:         R-CRAN-Metrics >= 0.1.4

%description
Frequently one needs a convenient way to build and tune several models in
one go.The goal is to provide a number of convenience functions useful in
machine learning applications. It provides the ability to build, tune and
obtain predictions of several models in one function. The models are built
using 'caret' functions with easier to read syntax. Kuhn(2014)
<arXiv:1405.6974v14>. Kuhn(2008) <doi10.18637/jss.v028.i05>.
Chambers,J.M.(1992) <doi:10.1371/journal.pone.0053143>. Wilkinson,G.N. and
Rogers, C. E. (1973) <doi:10.2307/2346786>.

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
