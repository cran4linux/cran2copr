%global packname  crmReg
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Cellwise Robust M-Regression and SPADIMO

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-pcaPP 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-rrcov 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-pcaPP 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-rrcov 

%description
Method for fitting a cellwise robust linear M-regression model (CRM,
Filzmoser et al. (2020) <DOI:10.1016/j.csda.2020.106944>) that yields both
a map of cellwise outliers consistent with the linear model, and a vector
of regression coefficients that is robust against vertical outliers and
leverage points. As a by-product, the method yields an imputed data set
that contains estimates of what the values in cellwise outliers would need
to amount to if they had fit the model. The package also provides
diagnostic tools for analyzing casewise and cellwise outliers using sparse
directions of maximal outlyingness (SPADIMO, Debruyne et al. (2019)
<DOI:10.1007/s11222-018-9831-5>).

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
