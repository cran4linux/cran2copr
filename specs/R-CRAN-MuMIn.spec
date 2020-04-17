%global packname  MuMIn
%global packver   1.43.17
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.43.17
Release:          1%{?dist}
Summary:          Multi-Model Inference

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-stats4 
BuildRequires:    R-nlme 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-Matrix 
Requires:         R-stats 
Requires:         R-stats4 
Requires:         R-nlme 

%description
Tools for performing model selection and model averaging. Automated model
selection through subsetting the maximum model, with optional constraints
for model inclusion. Model parameter and prediction averaging based on
model weights derived from information criteria (AICc and alike) or custom
model weighting schemes.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/TODO
%{rlibdir}/%{packname}/INDEX
