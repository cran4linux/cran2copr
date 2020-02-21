%global packname  SAMBA
%global packver   0.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0
Release:          1%{?dist}
Summary:          Selection and Misclassification Bias Adjustment for LogisticRegression Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-survey 
Requires:         R-stats 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-survey 

%description
Health research using data from electronic health records (EHR) has gained
popularity, but misclassification of EHR-derived disease status and lack
of representativeness of the study sample can result in substantial bias
in effect estimates and can impact power and type I error for association
tests. Here, the assumed target of inference is the relationship between
binary disease status and predictors modeled using a logistic regression
model. 'SAMBA' implements several methods for obtaining bias-corrected
point estimates along with valid standard errors as proposed in Beesley
and Mukherjee (2020) <doi:10.1101/2019.12.26.19015859>, currently under
review.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
