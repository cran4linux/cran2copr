%global __brp_check_rpaths %{nil}
%global packname  miselect
%global packver   0.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0
Release:          3%{?dist}%{?buildtag}
Summary:          Variable Selection for Multiply Imputed Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch

%description
Penalized regression methods, such as lasso and elastic net, are used in
many biomedical applications when simultaneous regression coefficient
estimation and variable selection is desired. However, missing data
complicates the implementation of these methods, particularly when
missingness is handled using multiple imputation. Applying a variable
selection algorithm on each imputed dataset will likely lead to different
sets of selected predictors, making it difficult to ascertain a final
active set without resorting to ad hoc combination rules. 'miselect'
presents Stacked Adaptive Elastic Net (saenet) and Grouped Adaptive LASSO
(galasso) for continuous and binary outcomes, developed by Du et al
(2020), currently under review. They, by construction, force selection of
the same variables across multiply imputed data. 'miselect' also provides
cross validated variants of these methods.

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
%{rlibdir}/%{packname}
