%global __brp_check_rpaths %{nil}
%global packname  WeightedROC
%global packver   2020.1.31
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2020.1.31
Release:          3%{?dist}%{?buildtag}
Summary:          Fast, Weighted ROC Curves

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Fast computation of Receiver Operating Characteristic (ROC) curves and
Area Under the Curve (AUC) for weighted binary classification problems
(weights are example-specific cost values).

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
