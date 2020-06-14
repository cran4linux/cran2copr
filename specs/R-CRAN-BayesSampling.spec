%global packname  BayesSampling
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          2%{?dist}
Summary:          Bayes Linear Estimators for Finite Population

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-stats 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-stats 

%description
Allows the user to apply the Bayes Linear approach to finite population
with the Simple Random Sampling - BLE_SRS() - and the Stratified Simple
Random Sampling design - BLE_SSRS() - (both without replacement) and to
the Ratio estimator (using auxiliary information) - BLE_Ratio(). The Bayes
linear estimation approach is applied to a general linear regression model
for finite population prediction in BLE_Reg() and it is also possible to
achieve the design based estimators using vague prior distributions. Based
on Gonçalves, K.C.M, Moura, F.A.S and Migon, H.S.(2014)
<https://www150.statcan.gc.ca/n1/en/catalogue/12-001-X201400111886>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
