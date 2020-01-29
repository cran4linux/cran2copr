%global packname  difNLR
%global packver   1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          1%{?dist}
Summary:          DIF and DDF Detection by Non-Linear Regression Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-CTT 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-VGAM 
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-CTT 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-CRAN-msm 
Requires:         R-nnet 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-reshape2 
Requires:         R-stats 
Requires:         R-CRAN-VGAM 

%description
Detection of differential item functioning (DIF) among dichotomously
scored items and differential distractor functioning (DDF) among unscored
items with non-linear regression procedures based on generalized logistic
regression models (Drabinova and Martinkova, 2017,
doi:10.1111/jedm.12158).

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DDF_CLRM_category.png
%doc %{rlibdir}/%{packname}/DDF_CLRM_cumulative.png
%doc %{rlibdir}/%{packname}/DIF_NLR.png
%{rlibdir}/%{packname}/INDEX
