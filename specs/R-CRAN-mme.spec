%global packname  mme
%global packver   0.1-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          3%{?dist}%{?buildtag}
Summary:          Multinomial Mixed Effects Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 1.8.0
Requires:         R-core >= 1.8.0
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-methods 

%description
Fit Gaussian Multinomial mixed-effects models for small area estimation:
Model 1, with one random effect in each category of the response variable
(Lopez-Vizcaino,E. et al., 2013) <doi:10.1177/1471082X13478873>; Model 2,
introducing independent time effect; Model 3, introducing correlated time
effect. mme calculates direct and parametric bootstrap MSE estimators
(Lopez-Vizcaino,E et al., 2014) <doi:10.1111/rssa.12085>.

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
%{rlibdir}/%{packname}/data
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CHANGES.txt
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
