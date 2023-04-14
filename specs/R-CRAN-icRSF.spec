%global __brp_check_rpaths %{nil}
%global packname  icRSF
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          3%{?dist}%{?buildtag}
Summary:          A Modified Random Survival Forest Algorithm

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.11.3
BuildRequires:    R-CRAN-icensmis 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp >= 0.11.3
Requires:         R-CRAN-icensmis 
Requires:         R-parallel 
Requires:         R-stats 

%description
Implements a modification to the Random Survival Forests algorithm for
obtaining variable importance in high dimensional datasets. The proposed
algorithm is appropriate for settings in which a silent event is observed
through sequentially administered, error-prone self-reports or laboratory
based diagnostic tests.  The modified algorithm incorporates a formal
likelihood framework that accommodates sequentially administered,
error-prone self-reports or laboratory based diagnostic tests. The
original Random Survival Forests algorithm is modified by the introduction
of a new splitting criterion based on a likelihood ratio test statistic.

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
