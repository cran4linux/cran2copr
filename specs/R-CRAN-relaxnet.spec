%global packname  relaxnet
%global packver   0.3-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}
Summary:          Relaxation of glmnet models (as in relaxed lasso, Meinshausen2007)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
Requires:         R-CRAN-glmnet 

%description
Extends the glmnet package with "relaxation", done by running glmnet once
on the entire predictor matrix, then again on each different subset of
variables from along the regularization path. Relaxation may lead to
improved prediction accuracy for truly sparse data generating models, as
well as fewer false positives (i.e. fewer noncontributing predictors in
the final model). Penalty may be lasso (alpha = 1) or elastic net (0 <
alpha < 1). For this version, family may be "gaussian" or "binomial" only.
Takes advantage of fast FORTRAN code from the glmnet package.

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
