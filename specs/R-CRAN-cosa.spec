%global __brp_check_rpaths %{nil}
%global packname  cosa
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Bound Constrained Optimal Sample Allocation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-msm >= 1.6.7
BuildRequires:    R-CRAN-nloptr >= 1.0.4
Requires:         R-CRAN-msm >= 1.6.7
Requires:         R-CRAN-nloptr >= 1.0.4

%description
Implements bound constrained optimal sample allocation (BCOSA) framework
described in Bulus & Dong (2019) <doi:10.1080/00220973.2019.1636197> for
power analysis of multilevel regression discontinuity designs (MRDDs) and
multilevel randomized trials (MRTs) with continuous outcomes. Separate
tools for statistical power and minimum detectable effect size
computations are provided.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
