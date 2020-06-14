%global packname  DTRlearn2
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          2%{?dist}
Summary:          Statistical Learning Methods for Optimizing Dynamic TreatmentRegimes

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-glmnet 
Requires:         R-CRAN-kernlab 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-glmnet 

%description
We provide a comprehensive software to estimate general K-stage DTRs from
SMARTs with Q-learning and a variety of outcome-weighted learning methods.
Penalizations are allowed for variable selection and model regularization.
With the outcome-weighted learning scheme, different loss functions - SVM
hinge loss, SVM ramp loss, binomial deviance loss, and L2 loss - are
adopted to solve the weighted classification problem at each stage;
augmentation in the outcomes is allowed to improve efficiency. The
estimated DTR can be easily applied to a new sample for individualized
treatment recommendations or DTR evaluation.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
