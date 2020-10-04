%global packname  normalr
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Normalisation of Multiple Variables in Large-Scale Datasets

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-shiny 
Requires:         R-MASS 
Requires:         R-parallel 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-shiny 

%description
The robustness of many of the statistical techniques, such as factor
analysis, applied in the social sciences rests upon the assumption of
item-level normality. However, when dealing with real data, these
assumptions are often not met. The Box-Cox transformation (Box & Cox,
1964) <http://www.jstor.org/stable/2984418> provides an optimal
transformation for non-normal variables. Yet, for large datasets of
continuous variables, its application in current software programs is
cumbersome with analysts having to take several steps to normalise each
variable. We present an R package 'normalr' that enables researchers to
make convenient optimal transformations of multiple variables in datasets.
This R package enables users to quickly and accurately: (1) anchor all of
their variables at 1.00, (2) select the desired precision with which the
optimal lambda is estimated, (3) apply each unique exponent to its
variable, (4) rescale resultant values to within their original X1 and
X(n) ranges, and (5) provide original and transformed estimates of
skewness, kurtosis, and other inferential assessments of normality.

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
%doc %{rlibdir}/%{packname}/shiny-examples
%{rlibdir}/%{packname}/INDEX
