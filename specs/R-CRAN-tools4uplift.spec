%global packname  tools4uplift
%global packver   0.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Tools for Uplift Modeling

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-glmnet 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-glmnet 

%description
Uplift modeling aims at predicting the causal effect of an action such as
a medical treatment or a marketing campaign on a particular individual, by
taking into consideration the response to a treatment. In order to
simplify the task for practitioners in uplift modeling, we propose a
combination of tools that can be separated into the following ingredients:
i) quantization, ii) visualization, iii) feature engineering, iv) feature
selection and, v) model validation. For more details, please read Belbahri
et Al. (2019)
<https://dms.umontreal.ca/~murua/research/UpliftRegression.pdf>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
