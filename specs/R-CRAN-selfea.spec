%global packname  selfea
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Select Features Reliably with Cohen's Effect Sizes

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pwr 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-pwr 
Requires:         R-MASS 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-ggplot2 

%description
Functions using Cohen's effect sizes (Cohen, Jacob. Statistical power
analysis for the behavioral sciences. Academic press, 2013) are provided
for reliable feature selection in biology data analysis.  In addition to
Cohen's effect sizes, p-values are calculated and adjusted from
quasi-Poisson GLM, negative binomial GLM and Normal distribution ANOVA.
Significant features (genes, RNAs or proteins) are selected by adjusted
p-value and minimum Cohen's effect sizes, calculated to keep certain level
of statistical power of biology data analysis given p-value threshold and
sample size.

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
