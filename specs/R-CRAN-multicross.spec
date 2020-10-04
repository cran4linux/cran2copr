%global packname  multicross
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          A Graph-Based Test for Comparing Multivariate Distributions inthe Multi Sample Framework

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3.49
BuildRequires:    R-stats >= 3.5.0
BuildRequires:    R-CRAN-nbpMatching >= 1.5.1
BuildRequires:    R-CRAN-crossmatch >= 1.3.1
BuildRequires:    R-Matrix >= 1.2.17
Requires:         R-MASS >= 7.3.49
Requires:         R-stats >= 3.5.0
Requires:         R-CRAN-nbpMatching >= 1.5.1
Requires:         R-CRAN-crossmatch >= 1.3.1
Requires:         R-Matrix >= 1.2.17

%description
We introduce a nonparametric, graphical test based on optimal matching for
assessing whether multiple unknown multivariate probability distributions
are equal. This method is consistent, and does not make any distributional
assumptions on the data. Our procedure combines data that belong to
different classes or groups to create a graph on the pooled data, and then
utilizes the number of edges connecting data points from different classes
to examine equality of distributions among the classes. The functions
available through this package implement the work described here:
<arXiv:1906.04776>.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
