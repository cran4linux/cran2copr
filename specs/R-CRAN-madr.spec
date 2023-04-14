%global __brp_check_rpaths %{nil}
%global packname  madr
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Model Averaged Double Robust Estimation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Estimates average treatment effects using model average double robust
(MA-DR) estimation. The MA-DR estimator is defined as weighted average of
double robust estimators, where each double robust estimator corresponds
to a specific choice of the outcome model and the propensity score model.
The MA-DR estimator extend the desirable double robustness property by
achieving consistency under the much weaker assumption that either the
true propensity score model or the true outcome model be within a
specified, possibly large, class of models.

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
