%global packname  ceterisParibus
%global packver   0.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.2
Release:          1%{?dist}
Summary:          Ceteris Paribus Profiles

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gower 
BuildRequires:    R-CRAN-DALEX 
BuildRequires:    R-CRAN-knitr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gower 
Requires:         R-CRAN-DALEX 
Requires:         R-CRAN-knitr 

%description
Ceteris Paribus Profiles (What-If Plots) are designed to present model
responses around selected points in a feature space. For example around a
single prediction for an interesting observation. Plots are designed to
work in a model-agnostic fashion, they are working for any predictive
Machine Learning model and allow for model comparisons. Ceteris Paribus
Plots supplement the Break Down Plots from 'breakDown' package.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
