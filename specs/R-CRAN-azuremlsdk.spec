%global packname  azuremlsdk
%global packver   0.5.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.7
Release:          1%{?dist}
Summary:          Interface to the 'Azure Machine Learning' 'SDK'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plyr >= 1.8
BuildRequires:    R-CRAN-reticulate >= 1.12
BuildRequires:    R-CRAN-rstudioapi >= 0.7
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-htmltools 
Requires:         R-CRAN-plyr >= 1.8
Requires:         R-CRAN-reticulate >= 1.12
Requires:         R-CRAN-rstudioapi >= 0.7
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-htmltools 

%description
Interface to the 'Azure Machine Learning' Software Development Kit
('SDK'). Data scientists can use the 'SDK' to train, deploy, automate, and
manage machine learning models on the 'Azure Machine Learning' service. To
learn more about 'Azure Machine Learning' visit the website:
<https://docs.microsoft.com/en-us/azure/machine-learning/service/overview-what-is-azure-ml>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
