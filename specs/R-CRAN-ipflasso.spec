%global packname  ipflasso
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Integrative Lasso with Penalty Factors

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-survival 
Requires:         R-CRAN-glmnet 
Requires:         R-survival 

%description
The core of the package is cvr2.ipflasso(), an extension of glmnet to be
used when the (large) set of available predictors is partitioned into
several modalities which potentially differ with respect to their
information content in terms of prediction. For example, in biomedical
applications patient outcome such as survival time or response to therapy
may have to be predicted based on, say, mRNA data, miRNA data, methylation
data, CNV data, clinical data, etc. The clinical predictors are on average
often much more important for outcome prediction than the mRNA data. The
ipflasso method takes this problem into account by using different penalty
parameters for predictors from different modalities. The ratio between the
different penalty parameters can be chosen from a set of optional
candidates by cross-validation or alternatively generated from the input
data.

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
