%global __brp_check_rpaths %{nil}
%global packname  azuremlsdk
%global packver   1.10.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.10.0
Release:          1%{?dist}%{?buildtag}
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
BuildRequires:    R-CRAN-servr 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinycssloaders 
Requires:         R-CRAN-plyr >= 1.8
Requires:         R-CRAN-reticulate >= 1.12
Requires:         R-CRAN-rstudioapi >= 0.7
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-servr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinycssloaders 

%description
Interface to the 'Azure Machine Learning' Software Development Kit
('SDK'). Data scientists can use the 'SDK' to train, deploy, automate, and
manage machine learning models on the 'Azure Machine Learning' service. To
learn more about 'Azure Machine Learning' visit the website:
<https://docs.microsoft.com/en-us/azure/machine-learning/service/overview-what-is-azure-ml>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
