%global packname  ggrisk
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}
Summary:          Risk Score Plot for Cox Regression

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-egg 
BuildRequires:    R-CRAN-do 
BuildRequires:    R-CRAN-set 
BuildRequires:    R-CRAN-cutoff 
BuildRequires:    R-CRAN-fastStat 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-CRAN-nomogramFormula 
Requires:         R-CRAN-ggplot2 
Requires:         R-survival 
Requires:         R-CRAN-egg 
Requires:         R-CRAN-do 
Requires:         R-CRAN-set 
Requires:         R-CRAN-cutoff 
Requires:         R-CRAN-fastStat 
Requires:         R-grid 
Requires:         R-CRAN-rms 
Requires:         R-CRAN-nomogramFormula 

%description
The risk plot may be one of the most commonly used figures in tumor
genetic data analysis. We can conclude the following two points: Comparing
the prediction results of the model with the real survival situation to
see whether the survival rate of the high-risk group is lower than that of
the low-level group, and whether the survival time of the high-risk group
is shorter than that of the low-risk group. The other is to compare the
heat map and scatter plot to see the correlation between the predictors
and the outcome.

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
