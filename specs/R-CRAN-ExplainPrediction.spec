%global __brp_check_rpaths %{nil}
%global packname  ExplainPrediction
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          3%{?dist}%{?buildtag}
Summary:          Explanation of Predictions for Classification and RegressionModels

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-semiArtificial >= 2.2.5
BuildRequires:    R-CRAN-CORElearn >= 1.52.0
Requires:         R-CRAN-semiArtificial >= 2.2.5
Requires:         R-CRAN-CORElearn >= 1.52.0

%description
Generates explanations for classification and regression models and
visualizes them. Explanations are generated for individual predictions as
well as for models as a whole. Two explanation methods are included,
EXPLAIN and IME. The EXPLAIN method is fast but might miss explanations
expressed redundantly in the model. The IME method is slower as it samples
from all feature subsets. For the EXPLAIN method see Robnik-Sikonja and
Kononenko (2008) <doi:10.1109/TKDE.2007.190734>, and the IME method is
described in Strumbelj and Kononenko (2010, JMLR, vol. 11:1-18). All
models in package 'CORElearn' are natively supported, for other prediction
models a wrapper function is provided and illustrated for models from
packages 'randomForest', 'nnet', and 'e1071'.

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
